def fcfs_scheduling():
    # Get the number of processes
    n = int(input("Enter number of processes: "))
    
    burst_time = []  # List to store burst times
    waiting_time = [0] * n  # Initialize waiting time list
    turnaround_time = [0] * n  # Initialize turnaround time list

    # Input burst times
    print("Enter Burst Time for each process:")
    for i in range(n):
        bt = int(input(f"Process P{i+1}: "))
        burst_time.append(bt)

    # Calculate waiting times
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

    # Calculate turnaround times
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n

    # Display results
    print("\nProcess | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"P{i+1}      | {burst_time[i]}         | {waiting_time[i]}           | {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

# Call the function to run
fcfs_scheduling()
