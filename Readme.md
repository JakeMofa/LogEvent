# LogEvent Benchmark (LifeCorporation Python Assessment)

This project was developed as part of a technical evaluation for the **Python + React Software Engineer** position at **LifeCorporation**.

##  Project Overview

The original challenge was to optimize a provided Python script (`LogEvent.py`) used to benchmark event logging performance. The original version logged one event at a time by opening and writing to a CSV file 100,000 times — a method that ran fine on Linux but performed poorly on Windows.

### The Task

1. Validate the script’s performance on Linux  
2. Run it on Windows and observe the difference  
3. Identify why Windows was significantly slower  
4. Optimize the script for speed — especially under Windows  
5. Submit the improved version along with analysis and test results  

---

##  What Was Done

 Optimized file I/O using **in-memory buffering**  
 Replaced repeated file writes with a single batch write  
 Implemented **try/except** error handling for file writing  
 Made output path **OS-agnostic and portable**  
 Added **command-line argument support** (`--count`, `--output`)  
 Wrote **unit tests** for `LogEvent()` and `Stack()` functions  

---

##  Performance Results

After refactoring, the script now runs under **1 second** on all platforms.

| Platform     | Before (Original)       | After (Optimized)     |
|--------------|--------------------------|------------------------|
| **Linux (Docker Ubuntu)** | 0.026s (already fast) | 0.388s (buffered, consistent) |
| **macOS (M1 MacBook Pro)** | 3.17s                   | 0.371s                 |
| **Windows 11 (Local Disk)** | 31.44s – 33.21s        | 0.700s                 |

---

##  Requirements

- Python 3.6 or higher
- No external packages required

---


## Usage

### Default Run (100,000 events):
```python logevent.py```

## Adding Unit Tests
```python testlogger.py```


### Design Notes
The updated script no longer hardcodes file paths. It writes output wherever the script is run, unless otherwise specified with --output.

Error handling is in place to handle file I/O failures gracefully.

The script is CLI-ready but still works with defaults if no args are passed.

Tested across macOS, Docker (Ubuntu), and Windows 11.



