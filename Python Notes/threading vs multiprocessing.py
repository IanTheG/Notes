# Advanced Python notes

"""
Advanced Threading vs. Multiprocessing

Process: an instance of a program
+ Takes advantage of multiple CPUs and cores
+ Can use multiple threads
+ Separate memory space => memory is not shared between processes
+ Great for CPU-bound processing
+ New process is stated independently from other processes
+ Processes are interruptable/killable
+ One GIL for each process => avoids GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread
- More memory
- IPC (inter-process communication) is more complicated

Threads: an entity within a process that can be scheduled for execution
A lightwight process

+ All threads within a process share the same memory
+ Lightweight
+ Starting a thread is faster than starting a process
+ Great for IO bound tasks

- Threading is limited by GIL: only one thread at a time
- No effect for CPU-bound tasks
- Not interruptable/killable
- Care with race conditions => two or more threads want to edit the same data at the same time

GIL: Global interpreter Lock
A lock in Python that allows only one thread at a time to execute in Python
Needed in CPython because memory management is not thread-safe

Avoid:
- Use multiprocessesing
- Use a different, free-threaded Python implementation
- Use Python as a wrapper for third-party libraries
"""

# FOR SOME REASON THIS DOES NOT WORK

from multiprocessing import Process
import os
import time

def funcProcesses(n):
    for i in range(n):
        i * i
        time.sleep(0.1)

processes_list: list[Process] = []
num_processes = os.cpu_count()

# Create processes
for i in range(num_processes):
    # Target function is executed by the process
    p = Process(target=funcProcesses, args=(10,))
    processes_list.append(p)

for p in processes_list:
    p.start()
# Waiting for all processes to finish, blocks main thread
for p in processes_list:
    p.join()


# THIS WORKS!

# Multi threading API
from threading import Thread
import time

def funcThreads(n):
    for i in range(n):
        i * i
        time.sleep(0.1)

threads_list: list[Thread] = []
num_threads = 10

# Create processes
for i in range(num_threads):
    # Target function is executed by the process
    t = Thread(target=funcThreads, args=(10,))
    threads_list.append(t)

for t in threads_list:
    t.start()
# Waiting for all processes to finish, blocks main thread
for t in threads_list:
    t.join()
