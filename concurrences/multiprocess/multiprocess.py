"""
A process is a running instance of a computer program.
Every Python program is executed in a Process, 
which is a new instance of the Python interpreter. 
Each Python process has one thread used to execute the program instructions 
called the MainThread. 
Both processes and threads are created and managed by the underlying 
operating system.

The multiprocessing.Pool is generally used for heterogeneous tasks, 
whereas multiprocessing.Process is generally used for homogeneous tasks.
"""

from multiprocessing import Process, current_process
from time import sleep

def task(sleep_time: int, message: str):
    sleep(sleep_time)
    print("Task {} executed by process {}".format(message, current_process()))


# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task, args=(1.5, 'New message from another process'))
    # run the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()

