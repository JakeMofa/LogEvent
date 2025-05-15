# Import the time, datetime, sys, traceback, pdb, and datetime modules
import time
import sys
import csv
import os
import argparse
from datetime import datetime

# Define a function to get the stack trace
def Stack():
    # Return a string containing the current function name
    curframe = sys._getframe()
    stackarr = [curframe.f_code.co_name]

    # Continue going up the stack until the main module is reached
    while True:
        curname = curframe.f_back.f_code.co_name
        if curname == "<module>":
            break
        stackarr.insert(0, curname)
        curframe = curframe.f_back

    # Return the stack trace as a string
    # after removing /LogEvent/Stack/
    return '/'.join(stackarr[:-2])

# Define a function to log an event
# LogEvent creates one log entry (does NOT write to disk here)
def LogEvent(event, start_time):
    # Get the current datetime as a string
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_time = time.time()
    elapsed = current_time - start_time
    stack = Stack()
    elapsed_str = f"{elapsed:.8f}" if 'e' not in str(elapsed) else f"{elapsed:8f}"
    return [event, elapsed_str, now_str, stack], current_time

def main():
     # Parse CLI arguments for --count and --output
    parser = argparse.ArgumentParser(description="Log Event Performance Test")
    parser.add_argument('--count', type=int, default=100000, help='Number of log events to generate')
    parser.add_argument('--output', type=str, default='writer1w.csv', help='Output CSV file path')
    args = parser.parse_args()
    
    # Define global variables to track the start time and the last time
    gnStartLog = time.time()
    gnStart = time.time()
    logs = []
    total_iterations = 100000

    # Use a try/except block to catch any unexpected disk I/O issues
    try:
        # Generate 100,000 log entries in memory (no I/O here)
        for _ in range(total_iterations):
            # Initialize variables and call LogEvent
            entry, gnStartLog = LogEvent("Hello walt this is an event!", gnStartLog)
            logs.append(entry)

        # Define a cross-platform output path (current working directory)
        output_path = os.path.join(os.getcwd(), 'writer1w.csv')

        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Open the file to append (in our case: write all at once for performance)
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerows(logs)

    except Exception as e:
        # Log fallback: print logs to console if writing fails
        print("Failed to write to file. Error:", e)
        for row in logs[:5]:
            print("Fallback Log Sample:", row)

    # Print total time taken and final event for validation
    total_time = time.time() - gnStart
    print(f"Total time: {total_time:.4f} seconds")
    print("Last event logged:", ','.join(f'"{item}"' for item in logs[-1]))

if __name__ == "__main__":
    main()
