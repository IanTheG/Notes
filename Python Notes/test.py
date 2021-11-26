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