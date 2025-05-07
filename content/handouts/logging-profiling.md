---
title: "Making it work: logging and profiling"
lecture: "10-logging-profiling"
weight: 10
---

## Profilers

### Shell

- [time](https://www.gnu.org/software/time/)
- [hyperfine](https://github.com/sharkdp/hyperfine)
- [perf-stat](https://man7.org/linux/man-pages/man1/perf-stat.1.html)
- [perf-record](https://man7.org/linux/man-pages/man1/perf-record.1.html)

### Python

- [timeit](https://docs.python.org/3/library/timeit.html)
- [yappi](https://github.com/sumerc/yappi)
- [CProfile](https://docs.python.org/3/library/profile.html)
- [line_profiler](https://github.com/pyutils/line_profiler)
- [py-spy](https://github.com/benfred/py-spy)

### Multi-lingual

There is a longer list of profiling tools available [here](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools)

## Code-examples

### Logging

- [`log_example.py`](code/python-scripts/log_example.py)
- [`log_example_mp.py`](code/python-scripts/log_example.py)
- [`log_example_mp_v2.py`](code/python-scripts/log_example_mp_v2.py)
- [`log_example_mp_v3.py`](code/python-scripts/log_example_mp_v3.py)

### Profilers

- [`cprofile_example.py`](code/python-scripts/cprofile_example.py)
- [`timeit_example.py`](code/python-scripts/timeit_example.py)
- [`yappi_example.py`](code/python-scripts/yappi_example.py)
- [`py_spy_example.py`](code/python-scripts/py_spy_example.py)
- [`custom_profile_example.py`](code/python-scripts/custom_profile_example.py)
- [`kernprof_example.py`](code/python-scripts/kernprof_example.py)

## Homework assignments

### Add logging

This homework assignment concerns implementing logging in a project. My recommendation is to do this
for the chat server that you are currently working on in the larger practical. Since logging will be
project wide, everyone will need to start using it in their implementations.

### Profile a program

For this task you should profile a program that actually takes time to execute and where
optimization might be possible. My recommendation is to profile the differential equation integrator
from the first practical task and the calculator from one of the homework assignments (it could also
be one of your current work projects). Use the profiling results to highlight where the program is
bottlenecked.

How we can use these results to optimize the code will be covered in later lectures.
