````markdown
# 🧪 Local Judge for Competitive Programming (Windows Compatible)

This is a simple **local judge** system for **Python** and **C++** programs, designed to run on **Windows** without relying on Linux-only tools.

It simulates an online judge: 
- Compiles (if C++)
- Runs test cases under time and memory constraints
- Compares output to expected answers
- Reports verdicts like `ACCEPTED`, `WRONG ANSWER`, `RUNTIME ERROR`, etc.

---

## ✅ Requirements(For localjudge.py)

### Python Environment
- Python 3.6 or newer
- Install dependencies using:

```bash
pip install psutil pyyaml
```
## ✅ Requirements(For localjudge.js)

### Node.js Environment
- Install Node.js
- Install dependencies using:

```bash
npm install js-yaml
```
````

### Optional (for C++ submissions)

* A working `g++` compiler (e.g., [MinGW-w64](https://www.mingw-w64.org/))
* Add `g++.exe` to your system PATH
* Test with:

```bash
g++ --version
```

---

## 📁 Folder Structure

Place all files inside a main directory (e.g., `mytask/`):

```
mytask/
├── limits.yaml
├── input/
│   ├── input01.txt
│   ├── input02.txt
├── answer/
│   ├── answer01.txt
│   ├── answer02.txt
├── submission/
│   ├── mycode.py       # Python solution
│   └── other.cpp       # Optional C++ solution
```

### Example: `limits.yaml`

```yaml
time_limit: 2       # in seconds
memory_limit: 256   # in MB
```

---

## 🚀 How to Use

1. Clone or copy this repo
2. Place your task folder as described above
3. Run the judge:

###Python file:

```bash
python -u "localjudge.py" -path <the_lab_no\lab_task_no>
```

##example:

```bash
python -u "localjudge.py" -path "Lab 1\Task B"
```

###Javascript file:

```bash
node localjudge.js -path <the_lab_no\lab_task_no>
```

##Example

```bash
node localjudge.js -path "Lab 1\Task A"
```


###DISCLAIMER
### => Your terminal path should be same as the `localjudge.py` directory!!!
---

## 🧾 Output Example

```
Judging mycode...
Test input01.txt: ACCEPTED [12ms, 5MB]
Test input02.txt: WRONG ANSWER [15ms, 6MB]

================== FINAL VERDICTS ==================
mycode: WRONG ANSWER
```

---

## ⚙️ Features

* Supports `.py` and `.cpp` submissions
* Uses actual time and peak memory tracking
* Handles timeouts, runtime errors, and compilation failures
* Works fully on Windows

---

## 📌 Notes

* Input/output comparison is whitespace-normalized
* C++ submissions require successful compilation via `g++`
* No Linux tools like `timeout`, `ulimit`, or `bash` are needed

---

## 📄 License

MIT License. Use freely in academic or personal projects.

```
