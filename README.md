# CPU Scheduling Visualizer

A Python-based Operating System project that simulates and visualizes popular CPU Scheduling Algorithms. The project calculates scheduling metrics, generates Gantt Charts, and compares algorithm performance using graphical analysis.

---

## Project Overview

CPU Scheduling is a fundamental concept in Operating Systems that determines how processes are allocated CPU time. This project implements multiple scheduling algorithms and provides visual insights into their execution.

The simulator helps users understand:

* Process execution order
* Waiting Time (WT)
* Turnaround Time (TAT)
* CPU scheduling efficiency
* Comparative algorithm analysis

---

## Implemented Algorithms

### First Come First Serve (FCFS)

Processes are executed in the order they arrive.

### Shortest Job First (SJF)

Processes with the smallest burst time are executed first.

### Round Robin (RR)

Processes are executed in cyclic order using a fixed time quantum.

### Priority Scheduling

Processes with higher priority are executed before lower-priority processes.

---

## Features

✔ Process Scheduling Simulation

✔ Waiting Time Calculation

✔ Turnaround Time Calculation

✔ Dynamic Gantt Chart Generation

✔ Performance Comparison Graphs

✔ Visualization using Matplotlib

✔ Object-Oriented Programming Approach

---

## Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Programming Language |
| Matplotlib   | Data Visualization        |
| OOP Concepts | Process Modeling          |

---

## Project Structure

```text
CPU-Scheduling-Visualizer/
│
├── cpu_scheduling.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── output.png
    ├── fcfs.png
    ├── sjf.png
    ├── rr.png
    ├── priority.png
    └── comparison.png
```

## Sample Input

| Process | Arrival Time | Burst Time | Priority |
| ------- | ------------ | ---------- | -------- |
| P1      | 0            | 5          | 2        |
| P2      | 1            | 3          | 1        |
| P3      | 2            | 8          | 3        |

---

## Output Metrics

The simulator computes:

* Waiting Time (WT)
* Turnaround Time (TAT)
* Average Waiting Time
* Average Turnaround Time

for every scheduling algorithm.

---


## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CPU-Scheduling-Visualizer.git
```

Move to project directory:

```bash
cd CPU-Scheduling-Visualizer
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python cpu_scheduling.py
```

---

## Future Enhancements

* Preemptive SJF Scheduling
* Preemptive Priority Scheduling
* Multi-Level Queue Scheduling
* Multi-Level Feedback Queue Scheduling
* GUI using Tkinter or PyQt
* Interactive Process Input System
* Export Results to CSV/PDF

---

## Learning Outcomes

This project demonstrates practical understanding of:

* Operating System Scheduling Concepts
* Data Structures
* Object-Oriented Programming
* Algorithm Analysis
* Data Visualization
* Python Application Development

---

## Author

Mahima Mishra

BCA Student

Passionate about Software Development, Data Structures, Operating Systems, Machine Learning, and Full-Stack Development.

---

## License

This project is licensed under the MIT License.
