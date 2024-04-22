from multiprocessing import Process
import os
import time
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# processes = []
#
# num_processes = os.cpu_count()
#
# # create processes
#
# print(num_processes)
#
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#
#
# # start
#
# for p in processes:
#     p.join()
#
# print("main")

from threading import Thread


threads = []

num_threads = os.cpu_count()

# create processes

print(num_threads)

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)


# start

for t in threads:
    t.start()

#join

for t in threads:
    t.join()

print("main")
