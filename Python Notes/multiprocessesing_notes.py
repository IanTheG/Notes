# Python Notes on Advanced topics

"""
Multiprocessing

- Recap how to create multiple processes
- Create and share data between processes
- Use Locks to prevent raise conditions
- Using Queues
- Use a pool to manage multiple processes

Process Pool
- Manages multiple processes
- Controls a pool of worker processes to which jobs can be submitted
- Manages processes for you
- Split data into smaller chunks to enable processing in parallel

Do NOT live in the same memory space, do NOT have access to the same data
Must use Value or Array to access shared data
"""

# Review this:

# from multiprocessing import Process
# import os

# def square_numbers(n):
#     for i in range(n):
#         i * i

# if __name__ == "__main__":
#     processes_list: list[Process] = []
#     num_processes = os.cpu_count()

#     # Create processes
#     for i in range(num_processes):
#         # Target function is executed by the process
#         p = Process(target=square_numbers, args=(10,))
#         processes_list.append(p)

#     for p in processes_list:
#         p.start()
#     # Waiting for all processes to finish, blocks main thread
#     for p in processes_list:
#         p.join()


# Value

# from multiprocessing import Process, Value, Lock
# import time

# def add_100(n, lock: Lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         n.value += 1
#         lock.release()

#     # Or as a content manager with "with"
#     # for i in range(100):
#     #      time.sleep(0.01)
#     #      with lock:
#     #         n.value += 1

# if __name__ == "__main__":
#     lock = Lock()

#     shared_number = Value('i', 0)
#     print("Number at beginning:", shared_number.value)

#     p1 = Process(target=add_100, args=(shared_number, lock))
#     p2 = Process(target=add_100, args=(shared_number, lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     # Often does not end at 200, a raise condition occurs
#     # Both processes attempt to read and write into the same object
#     # Some operations / function calls are lost
#     # Use a Lock
#     print("Number at end:", shared_number.value)


# # Array

# from multiprocessing import Process, Array, Lock
# import time

# def add_100_toeach(nums, lock: Lock):
#     for i in range(100):
#         time.sleep(0.01)
#         for i in range(len(nums)):
#             with lock: # Use a lock to ensure all elements of array have +100
#                 nums[i] += 1

# if __name__ == "__main__":
#     lock = Lock()

#     shared_list = Array('d', [0.0, 100.0, 200.0])
#     print("Array at beginning:", shared_list[:])

#     p1 = Process(target=add_100_toeach, args=(shared_list, lock))
#     p2 = Process(target=add_100_toeach, args=(shared_list, lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     # Often does not end at 200, a raise condition occurs
#     # Both processes attempt to read and write into the same object
#     # Some operations / function calls are lost
#     # Use a Lock
#     print("Array at end:", shared_list[:])


# # Using Queues to exchange data

# from multiprocessing import Process, Array, Lock
# from multiprocessing import Queue # First in, first out data structure
# import time

# def square(nums, q: Queue):
#     for i in nums:
#         q.put(i*i)

# def negate(nums, q: Queue):
#     for i in nums:
#         q.put(-1*i)

# if __name__ == "__main__":
#     nums = range(1, 6)
#     q = Queue()

#     p1 = Process(target=square, args=(nums, q))
#     p2 = Process(target=negate, args=(nums, q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     # You can access the queue in the main process too
#     while not q.empty():
#         print(q.get())


# Process Pool

from multiprocessing import Pool

def cube(num):
    return num * num * num

if __name__ == "__main__":
    nums = range(10)
    pool = Pool()

    # Map, Apply, Join, Close methods

    # Automatically allocates the max number of available processes and creates them
    # Creates as many processes as cores on the computer!
    # Splits iterable data (nums) into equal sized chucks and sent into the function (cube)
    # Function is executed in parallel in different processes
    # .map blocks the main program until the result from cube is completed
    result = pool.map(cube, nums)

    # Can use .imap to return results from cube as soon as it is ready

    # If you only want one process to be executed by a pool, use .apply()
    # Put arguments in a tuple
    pool.apply(cube, (nums[0],))

    # Can use asynchronous versions of .map_async and .apply_async to NOT block the main thread

    pool.close()
    pool.join() # Waits for pool to complete before printing result!

    print(result)
