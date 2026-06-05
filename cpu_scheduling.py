import matplotlib.pyplot as plt

# -------------------------------
# Process Class
# -------------------------------
class Process:
    def __init__(self, pid, at, bt, priority=0):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.priority = priority


# -------------------------------
# FCFS Scheduling
# -------------------------------
def fcfs(processes):
    processes.sort(key=lambda x: x.at)
    time = 0
    gantt = []
    wt, tat = {}, {}

    for p in processes:
        if time < p.at:
            time = p.at

        start = time
        time += p.bt
        end = time

        gantt.append((p.pid, start, end))

        wt[p.pid] = start - p.at
        tat[p.pid] = end - p.at

    return gantt, wt, tat


# -------------------------------
# SJF (Non-Preemptive)
# -------------------------------
def sjf(processes):
    time = 0
    completed = []
    gantt = []
    wt, tat = {}, {}

    processes = sorted(processes, key=lambda x: x.at)
    ready = []

    while len(completed) < len(processes):
        for p in processes:
            if p.at <= time and p not in ready and p not in completed:
                ready.append(p)

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.bt)
        p = ready.pop(0)

        start = time
        time += p.bt
        end = time

        gantt.append((p.pid, start, end))

        wt[p.pid] = start - p.at
        tat[p.pid] = end - p.at

        completed.append(p)

    return gantt, wt, tat


# -------------------------------
# Round Robin
# -------------------------------
def round_robin(processes, tq):
    time = 0
    queue = []
    gantt = []
    rem_bt = {p.pid: p.bt for p in processes}
    wt = {p.pid: 0 for p in processes}
    tat = {}

    processes = sorted(processes, key=lambda x: x.at)
    i = 0

    while True:
        while i < len(processes) and processes[i].at <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            if i < len(processes):
                time = processes[i].at
                continue
            else:
                break

        p = queue.pop(0)
        start = time

        if rem_bt[p.pid] > tq:
            time += tq
            rem_bt[p.pid] -= tq
            gantt.append((p.pid, start, time))
        else:
            time += rem_bt[p.pid]
            gantt.append((p.pid, start, time))
            tat[p.pid] = time - p.at
            wt[p.pid] = tat[p.pid] - p.bt
            rem_bt[p.pid] = 0

        while i < len(processes) and processes[i].at <= time:
            queue.append(processes[i])
            i += 1

        if rem_bt[p.pid] > 0:
            queue.append(p)

    return gantt, wt, tat


# -------------------------------
# Priority Scheduling (Non-Preemptive)
# -------------------------------
def priority_scheduling(processes):
    time = 0
    completed = []
    gantt = []
    wt, tat = {}, {}

    while len(completed) < len(processes):
        ready = [p for p in processes if p.at <= time and p not in completed]

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.priority)  # lower = higher priority
        p = ready[0]

        start = time
        time += p.bt
        end = time

        gantt.append((p.pid, start, end))

        wt[p.pid] = start - p.at
        tat[p.pid] = end - p.at

        completed.append(p)

    return gantt, wt, tat


# -------------------------------
# Gantt Chart Plot
# -------------------------------
def plot_gantt(gantt, title):
    fig, ax = plt.subplots()

    for i, (pid, start, end) in enumerate(gantt):
        ax.barh(pid, end - start, left=start)

    ax.set_xlabel("Time")
    ax.set_title(title)
    plt.show()


# -------------------------------
# Comparison Graph
# -------------------------------
def compare(avg_wt, avg_tat):
    algos = list(avg_wt.keys())

    wt_vals = list(avg_wt.values())
    tat_vals = list(avg_tat.values())

    x = range(len(algos))

    plt.bar(x, wt_vals)
    plt.xticks(x, algos)
    plt.title("Average Waiting Time Comparison")
    plt.show()

    plt.bar(x, tat_vals)
    plt.xticks(x, algos)
    plt.title("Average Turnaround Time Comparison")
    plt.show()


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5, 2),
        Process("P2", 1, 3, 1),
        Process("P3", 2, 8, 3)
    ]

    avg_wt = {}
    avg_tat = {}

    # FCFS
    g, wt, tat = fcfs(processes.copy())
    print("\nFCFS:", wt, tat)
    plot_gantt(g, "FCFS")
    avg_wt["FCFS"] = sum(wt.values()) / len(wt)
    avg_tat["FCFS"] = sum(tat.values()) / len(tat)

    # SJF
    g, wt, tat = sjf(processes.copy())
    print("\nSJF:", wt, tat)
    plot_gantt(g, "SJF")
    avg_wt["SJF"] = sum(wt.values()) / len(wt)
    avg_tat["SJF"] = sum(tat.values()) / len(tat)

    # Round Robin
    g, wt, tat = round_robin(processes.copy(), 2)
    print("\nRound Robin:", wt, tat)
    plot_gantt(g, "Round Robin")
    avg_wt["RR"] = sum(wt.values()) / len(wt)
    avg_tat["RR"] = sum(tat.values()) / len(tat)

    # Priority
    g, wt, tat = priority_scheduling(processes.copy())
    print("\nPriority:", wt, tat)
    plot_gantt(g, "Priority")
    avg_wt["Priority"] = sum(wt.values()) / len(wt)
    avg_tat["Priority"] = sum(tat.values()) / len(tat)

    # Comparison
    compare(avg_wt, avg_tat)
