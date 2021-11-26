# Python Notes on Advanced topics

"""
Multithreading, Queues

Features
- Threads access the same memory space, can access the same data

from threading import Thread

def funcThreads(n):
    for i in range(n):
        i * i

if __name__ == "__main__":
    threads_list: list[Thread] = []
    num_threads = 10

    # Create processes
    for i in range(num_threads):
        # Target function is executed by the process
        t = Thread(target=funcThreads, args=(10,))
        threads_list.append(t)

    # Start threads
    for t in threads_list:
        t.start()
    # Waiting for all processes to finish, blocks main thread
    for t in threads_list:
        t.join()
    
    print("end main")

"""

# Sharing the same data between threads

from threading import Thread, Lock
import threading
import time

database_value = 0

def increase(lock: Lock):
    global database_value

    lock.acquire() # block the lock!

    # Make a new copy of the "state" or database and modify it
    local_copy = database_value
    local_copy += 1

    # Simulate a long process, python switches to other thread
    time.sleep(0.1)
    # Update database value
    database_value = local_copy

    lock.release() # release the lock!

    # Or us lock as a context manage with "with"
    # No need to use .acquire() or .release()
    # with lock:
    #     local_copy = database_value
    #     local_copy += 1
    #     time.sleep(0.1)
    #     database_value = local_copy

if __name__ == "__main__":
    print("start value", database_value)

    lock = Lock()

    # Pass a Lock to prevent another thread from accessing
    # the same code at the same time
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    
    print("end value", database_value) 
    # we expect 2, but result is 1
    # the second process does not wait until the first is finished
    # before modifying the global variable!
    # use lock


# Using a queue

from queue import Queue

if __name__ == "__main__":
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    # Returns and removes the first item
    first = q.get()
    print(first)

    # Returns true if queue is empty
    q.empty()

    # Tells python that processing is done with q
    q.task_done()

    # Blocks execution in the main thread until all items in queue are processed
    q.join()


# Example

from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q: Queue, lock: Lock):
    while True: # Infinite loop!!!
        # Blocks and waits until items in the q are available
        value = q.get() # Thread safe! No other thread can access this data

        with lock: # Use a Lock to ensure thread safety
            print(f'In {current_thread().name} got {value}')

        q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        # A background thread that dies when the main thread dies
        # Kills the infinite loop in the worker() method!
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i) # Thread safe! No other thread can access this data

    # Blocks main thread until all items are processed!
    q.join()

    print("End main")
