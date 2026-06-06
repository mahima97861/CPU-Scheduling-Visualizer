# ⚙️ CPU Scheduling Algorithm Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Operating Systems](https://img.shields.io/badge/Operating%20Systems-Scheduling-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

The **CPU Scheduling Algorithm Simulator** is a Python-based Operating Systems project that demonstrates the implementation and performance analysis of fundamental CPU scheduling algorithms.

The simulator executes multiple scheduling strategies, generates Gantt Charts for process execution visualization, and compares algorithm efficiency using Average Waiting Time and Average Turnaround Time metrics.

This project provides practical insights into process management and scheduling concepts used by modern operating systems.

---

## 🎯 Objectives

* Simulate common CPU Scheduling Algorithms.
* Visualize process execution using Gantt Charts.
* Compare scheduling performance.
* Analyze Waiting Time and Turnaround Time.
* Understand Operating System process scheduling concepts.

---

## ✨ Features

✅ First Come First Serve (FCFS)

✅ Shortest Job First (SJF)

✅ Round Robin Scheduling

✅ Priority Scheduling

✅ Automatic Waiting Time Calculation

✅ Turnaround Time Analysis

✅ Gantt Chart Visualization

✅ Comparative Performance Graphs

✅ Process Management Simulation

---

## 🛠️ Technologies Used

| Technology            | Purpose            |
| --------------------- | ------------------ |
| Python                | Core Development   |
| Matplotlib            | Data Visualization |
| OOP                   | Process Modeling   |
| Scheduling Algorithms | CPU Management     |
| Data Structures       | Queue Handling     |

---

## 📚 Implemented Algorithms

### 1️⃣ First Come First Serve (FCFS)

Processes are executed in the order of arrival.

Characteristics:

* Simple implementation
* Non-preemptive
* May suffer from convoy effect

---

### 2️⃣ Shortest Job First (SJF)

The process with the shortest burst time is executed first.

Characteristics:

* Minimizes average waiting time
* Non-preemptive implementation
* Requires burst time prediction

---

### 3️⃣ Round Robin (RR)

Each process receives a fixed time quantum.

Characteristics:

* Fair CPU allocation
* Preemptive scheduling
* Suitable for time-sharing systems

---

### 4️⃣ Priority Scheduling

Processes are executed according to assigned priority.

Characteristics:

* Higher priority tasks execute first
* Supports critical process handling
* May cause starvation

---

## 🔄 System Workflow

Process Creation

⬇️

Algorithm Selection

⬇️

Scheduling Execution

⬇️

Gantt Chart Generation

⬇️

Performance Evaluation

⬇️

Comparative Analysis

---

## 📥 Sample Process Set

| Process | Arrival Time | Burst Time | Priority |
| ------- | ------------ | ---------- | -------- |
| P1      | 0            | 5          | 2        |
| P2      | 1            | 3          | 1        |
| P3      | 2            | 8          | 3        |

---

## 📊 Output Metrics

The simulator calculates:

* Waiting Time (WT)
* Turnaround Time (TAT)
* Average Waiting Time
* Average Turnaround Time

---

## 📈 Visualizations

### Gantt Charts

The project generates execution timelines for:

* FCFS
* SJF
* Round Robin
* Priority Scheduling

### Comparison Graphs

Performance comparison based on:

* Average Waiting Time
* Average Turnaround Time

---

## 📂 Project Structure

```text
CPU-Scheduling-Algorithm-Simulator/
│
├── cpu_scheduling.py
│
├── screenshots/
│   ├── fcfs.png
│   ├── sjf.png
|   ├── output.png
|   ├── WT_comparison.png
│   ├── round_robin.png
│   ├── priority.png
│   └── TAT_comparison.png
│
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cpu-scheduling-algorithm-simulator.git
```

Navigate to project folder:

```bash
cd cpu-scheduling-algorithm-simulator
```

Install dependencies:

```bash
pip install matplotlib
```

Run the application:

```bash
python scheduler.py
```

---

## 📊 Time Complexity

| Algorithm           | Complexity |
| ------------------- | ---------- |
| FCFS                | O(n)       |
| SJF                 | O(n²)      |
| Round Robin         | O(n × q)   |
| Priority Scheduling | O(n²)      |

---

## 🎓 Learning Outcomes

Through this project, I gained hands-on experience in:

* Operating System Concepts
* CPU Scheduling Techniques
* Process Management
* Queue Management
* Performance Evaluation
* Python Programming
* Data Visualization
* Algorithm Analysis

---

## 🔮 Future Enhancements

* GUI Dashboard using Tkinter
* Interactive User Input
* Preemptive SJF
* Multi-Level Queue Scheduling
* Multi-Level Feedback Queue
* Real-Time Scheduling Algorithms
* Export Results to CSV
* Web-Based Visualization Dashboard

---

## 👩‍💻 Author

### Mahima Mishra

BCA Student

Python Developer

Operating Systems Enthusiast

Passionate about Software Development and Problem Solving

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
