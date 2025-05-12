def sjf_scheduling():
    # Taking input for the number of processes
    n = int(input("Enter number of processes: "))
    
    processes = []  # List to store (process ID, burst time)
    
    # Input burst times
    print("Enter Burst Time for each process:")
    for i in range(n):
        burst_time = int(input(f"Process P{i+1}: "))
        processes.append((i+1, burst_time))  # Store (Process ID, Burst Time)
    
    # Sorting based on burst time (SJF)
    processes.sort(key=lambda x: x[1])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculating waiting times
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]
    
    # Calculating turnaround times
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]
    
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n
    
    # Display results
    print("\nProcess | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}      | {processes[i][1]}         | {waiting_time[i]}           | {turnaround_time[i]}")
    
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

# Call the function to run
sjf_scheduling()
