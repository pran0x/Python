#include <stdio.h>
void sjf();
int main() {
    sjf();
    return 0;
}

void sjf() {
    // Taking input for the number of processes;
    printf("Enter number of processes: ");
    int n;
    scanf("%d", &n);

    int processes[n], burst_time[n], waiting_time[n], turnaround_time[n];

    // Input burst times
    printf("Enter Burst Time for each process:\n");
    for (int i = 0; i < n; i++) {
        printf("Process P%d: ", i + 1); // for starting index from 1 
        scanf("%d", &burst_time[i]);
        processes[i] = i + 1; // Store process ID;
    }

    // Sorting based on burst time (SJF)
    for (int i = 0; i < n - 1; i++) { 
        for (int j = i + 1; j < n; j++) {
            if (burst_time[i] > burst_time[j]) {
                // Swap burst time
                int temp = burst_time[i];
                burst_time[i] = burst_time[j];
                burst_time[j] = temp;

                // Swap process ID
                temp = processes[i];
                processes[i] = processes[j];
                processes[j] = temp;
            }
        }
    }

    // Calculating waiting times;
    waiting_time[0] = 0;
    for (int i = 1; i < n; i++) {
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1];
    }

    // Calculating turnaround times;
    for (int i = 0; i < n; i++) {
        turnaround_time[i] = waiting_time[i] + burst_time[i];
    }

    // Calculating averages;
    float avg_wt = 0, avg_tat = 0;
    for (int i = 0; i < n; i++) {
        avg_wt += waiting_time[i];
        avg_tat += turnaround_time[i];
    }
    avg_wt /= n;
    avg_tat /= n;

    // Display results;
    printf("\nProcess | Burst Time | Waiting Time | Turnaround Time\n");
    for (int i = 0; i < n; i++) {
        printf("P%d      | %d         | %d           | %d\n", processes[i], burst_time[i], waiting_time[i], turnaround_time[i]);
    }

    printf("\nAverage Waiting Time: %.2f\n", avg_wt);
    printf("Average Turnaround Time: %.2f\n", avg_tat);
}
