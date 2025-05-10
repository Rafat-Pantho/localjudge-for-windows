import subprocess
import os
import sys
import time
import yaml
import glob
import difflib
import psutil
import threading

from pathlib import Path

def load_limits(task_path):
    with open(os.path.join(task_path, "limits.yaml"), 'r') as f:
        limits = yaml.safe_load(f)
    return limits['time_limit'], limits['memory_limit']

def normalize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().strip().splitlines()
    return [line.strip() for line in lines if line.strip()]

def run_with_limits(command, input_data, time_limit, memory_limit):
    result = {
        "output": "",
        "status": "ACCEPTED",
        "time_ms": 0,
        "memory_mb": 0
    }

    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p = psutil.Process(proc.pid)

    peak_memory = 0
    start_time = time.time()

    def feed_input():
        try:
            proc.stdin.write(input_data)
            proc.stdin.close()
        except Exception:
            pass

    input_thread = threading.Thread(target=feed_input)
    input_thread.start()

    while True:
        if proc.poll() is not None:
            break
        try:
            mem = p.memory_info().rss // (1024 * 1024)
            peak_memory = max(peak_memory, mem)
        except psutil.NoSuchProcess:
            break
        if (time.time() - start_time) > time_limit:
            proc.kill()
            result["status"] = "TIME/MEMORY LIMIT EXCEEDED"
            break
        time.sleep(0.01)  # 10ms poll interval

    end_time = time.time()
    result["time_ms"] = int((end_time - start_time) * 1000)
    result["memory_mb"] = peak_memory

    if result["status"] == "TIME/MEMORY LIMIT EXCEEDED":
        return result

    try:
        out, err = proc.communicate(timeout=1)
        if proc.returncode != 0:
            result["status"] = "RUNTIME ERROR"
        else:
            result["output"] = out
    except subprocess.TimeoutExpired:
        proc.kill()
        result["status"] = "RUNTIME ERROR"

    return result


def judge(task_path):
    time_limit, memory_limit = load_limits(task_path)
    input_files = sorted(glob.glob(f"{task_path}/input/input*.txt"))
    answer_files = sorted(glob.glob(f"{task_path}/answer/answer*.txt"))
    submissions = sorted(glob.glob(f"{task_path}/submission/*.py")) + sorted(glob.glob(f"{task_path}/submission/*.cpp"))

    verdicts = []

    for source_file in submissions:
        base = os.path.splitext(os.path.basename(source_file))[0]
        print(f"Judging {base}...")

        is_cpp = source_file.endswith('.cpp')
        if is_cpp:
            executable = os.path.join(task_path, f"{base}.exe")
            compile_cmd = ["g++", source_file, "-o", executable]
            try:
                subprocess.run(compile_cmd, check=True, capture_output=True)
            except subprocess.CalledProcessError:
                print(f"{base}: COMPILATION ERROR")
                verdicts.append((base, "COMPILATION ERROR"))
                continue
            command = [executable]
        else:
            command = ["python", source_file]

        highest_verdict = "ACCEPTED"
        for in_file, ans_file in zip(input_files, answer_files):
            with open(in_file, 'r', encoding='utf-8') as f:
                input_data = f.read()

            expected_output = normalize_file(ans_file)
            result = run_with_limits(command, input_data, time_limit, memory_limit)

            actual_output = result["output"].splitlines()
            actual_output = [line.strip() for line in actual_output if line.strip()]

            if result["status"] != "ACCEPTED":
                verdict = result["status"]
            elif actual_output != expected_output:
                verdict = "WRONG ANSWER"
            else:
                verdict = "ACCEPTED"

            status_line = f"Test {os.path.basename(in_file)}: {verdict} [{result['time_ms']}ms, {result['memory_mb']}MB]"
            print(status_line)

            if verdict != "ACCEPTED" and verdict != highest_verdict:
                highest_verdict = verdict

        print()
        verdicts.append((base, highest_verdict))
        if is_cpp:
            os.remove(executable)

    print("================== FINAL VERDICTS ==================")
    for name, v in verdicts:
        print(f"{name}: {v}")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "-path":
        print("Usage: python localjudge.py -path <path_to_task_directory>")
        sys.exit(1)
    judge(sys.argv[2])
