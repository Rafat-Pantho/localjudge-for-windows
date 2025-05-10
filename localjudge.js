const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");
const { spawn, execSync } = require("child_process");

const normalize = (text) =>
  text.trim().split(/\r?\n/).map(line => line.trim()).filter(Boolean).join("\n");

function getMemoryMB(pid) {
  try {
    const output = execSync(`wmic process where ProcessId=${pid} get WorkingSetSize /value`, { stdio: ["pipe", "pipe", "ignore"] });
    const match = output.toString().match(/WorkingSetSize=(\d+)/);
    if (match) {
      const bytes = parseInt(match[1], 10);
      return Math.round(bytes / 1024 / 1024);
    }
  } catch (e) {}
  return 0;
}

function execWithMetrics(command, args = [], options = {}) {
  return new Promise((resolve) => {
    const start = Date.now();
    const child = spawn(command, args, { stdio: "pipe", shell: false });

    let stdout = "";
    let stderr = "";
    let timedOut = false;
    let peakMemory = 0;

    const timer = setTimeout(() => {
      timedOut = true;
      child.kill("SIGKILL");
    }, options.timeout || 2000);

    if (options.input) {
      child.stdin.write(options.input);
    }
    child.stdin.end();

    const memoryInterval = setInterval(() => {
      const mem = getMemoryMB(child.pid);
      peakMemory = Math.max(peakMemory, mem);
    }, 50); // every 50ms

    child.stdout.on("data", (data) => {
      stdout += data.toString();
    });

    child.stderr.on("data", (data) => {
      stderr += data.toString();
    });

    child.on("close", (code) => {
      clearInterval(memoryInterval);
      clearTimeout(timer);
      const duration = Date.now() - start;

      if (timedOut) {
        resolve({ status: "TIME LIMIT EXCEEDED", stdout, stderr, time: duration, memory: peakMemory });
      } else if (code !== 0) {
        resolve({ status: "RUNTIME ERROR", stdout, stderr, time: duration, memory: peakMemory });
      } else {
        resolve({ status: "OK", stdout, stderr, time: duration, memory: peakMemory });
      }
    });

    child.on("error", (err) => {
      clearInterval(memoryInterval);
      clearTimeout(timer);
      resolve({ status: "RUNTIME ERROR", stdout, stderr: stderr + err.message, time: 0, memory: 0 });
    });
  });
}

async function judge(taskPath) {
  const limits = yaml.load(fs.readFileSync(path.join(taskPath, "limits.yaml"), "utf8"));
  const timeLimit = (limits.time_limit || 2) * 1000;

  const inputDir = path.join(taskPath, "input");
  const answerDir = path.join(taskPath, "answer");
  const subDir = path.join(taskPath, "submission");

  const inputFiles = fs.readdirSync(inputDir).filter(f => f.startsWith("input")).sort();
  const answerFiles = fs.readdirSync(answerDir).filter(f => f.startsWith("answer")).sort();
  const submissions = fs.readdirSync(subDir).filter(f => f.endsWith(".py") || f.endsWith(".cpp"));

  for (const file of submissions) {
    const base = path.basename(file, path.extname(file));
    const fullPath = path.join(subDir, file);
    console.log(`\nJudging ${file}...`);

    let cmd = [], isCpp = file.endsWith(".cpp"), tempExe = "";
    if (isCpp) {
      tempExe = path.join(taskPath, `${base}.exe`);
      try {
        const compile = spawn("g++", [fullPath, "-o", tempExe]);
        await new Promise((resolve, reject) => {
          compile.on("close", (code) => {
            if (code !== 0) reject("COMPILATION ERROR");
            else resolve();
          });
        });
        cmd = [tempExe];
      } catch {
        console.log(`${file}: COMPILATION ERROR`);
        continue;
      }
    } else {
      cmd = ["python", fullPath];
    }

    let finalVerdict = "ACCEPTED";

    for (let i = 0; i < inputFiles.length; i++) {
      const input = fs.readFileSync(path.join(inputDir, inputFiles[i]), "utf8");
      const expected = normalize(fs.readFileSync(path.join(answerDir, answerFiles[i]), "utf8"));

      const result = await execWithMetrics(cmd[0], cmd.slice(1), {
        input,
        timeout: timeLimit
      });

      const output = normalize(result.stdout);
      let verdict = result.status === "OK" ? (output === expected ? "ACCEPTED" : "WRONG ANSWER") : result.status;

      const msg = `Test ${i + 1}: ${verdict} [${result.time}ms, ${result.memory}MB]`;
      console.log(msg);

      if (verdict !== "ACCEPTED") finalVerdict = verdict;
    }

    console.log(`Final verdict for ${file}: ${finalVerdict}`);

    if (isCpp && fs.existsSync(tempExe)) fs.unlinkSync(tempExe);
  }
}

if (process.argv.length !== 4 || process.argv[2] !== "-path") {
  console.log("Usage: node localjudge.js -path <task_directory>");
  process.exit(1);
}

judge(process.argv[3]);
