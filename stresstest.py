import os
import time
import multiprocessing
import psutil
import argparse

# This function will be run in each process
def stress_cpu(duration):
    # The end time is duration seconds from the start
    end_time = time.time() + duration

    # Continuously perform a math operation until the end time
    while time.time() < end_time:
        x = 0
        # This operation is just meant to keep the CPU busy
        while x < 1000000:
            x = x**x
            x += 1

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Run a CPU stress test")
    # Add duration argument
    parser.add_argument("-d", "--duration", type=int, default=60, help="Duration of the stress test in seconds")
    # Parse arguments
    args = parser.parse_args()

    # Get the number of CPUs available
    num_cpus = os.cpu_count()

    # Get the initial CPU load
    # The argument to cpu_percent is the number of seconds over which to calculate CPU usage
    cpu_load_before = psutil.cpu_percent(interval=1)

    # Create a list to hold the processes
    processes = []

    # Start the processes
    # We start as many processes as there are CPUs
    for i in range(num_cpus):
        # Each process will run the stress_cpu function
        p = multiprocessing.Process(target=stress_cpu, args=(args.duration,))
        p.start()
        processes.append(p)

    # Wait for all the processes to finish
    # join() blocks until the process finishes
    for p in processes:
        p.join()

    # Get the CPU load after the stress test
    cpu_load_after = psutil.cpu_percent(interval=1)

    # Print the CPU load before and after the stress test
    print(f"CPU load before stress test: {cpu_load_before}%")
    print(f"CPU load after stress test: {cpu_load_after}%")

