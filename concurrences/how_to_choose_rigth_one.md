# Which Python Concurrency API Should You Use?

[source: superfastpython](https://superfastpython.com/python-concurrency-choose-api/)

You want to use concurrency in your Python program.

*There’s just one problem. Which API should you use?*

You’re not alone. This is perhaps one of the most common questions I receive.
That’s why I wrote this guide.

Firstly, there are three main Python concurrency APIs, they are:

- Coroutine-based, provided by the “asyncio” module.
- Thread-based, provided by the “threading” module.
- Process-based, provided by the “multiprocessing” module.

![](https://i0.wp.com/superfastpython.com/wp-content/uploads/2022/07/Python-Concurrency-API-Choice.jpg?ssl=1)


## The steps are as follows:

Step 1: CPU-Bound vs IO-Bound (Multiprocessing vs Threading)
Step 1.1 Choosing Between AsyncIO and Threading
Step 2: Many Ad Hoc Tasks vs One Complex Task?
Step 3: Pools vs Executors?

![](https://i0.wp.com/superfastpython.com/wp-content/uploads/2022/07/Python-Concurrency-API-Decision-Tree.jpg?ssl=1)

## CPU-Bound Tasks
A CPU-bound task is a type of task that involves performing a computation and does not involve IO.

The operations only involve data in main memory and performing computations on or with that data.

As such, the limit on these operations is the speed of the CPU. This is why we call them CPU-bound tasks.

Examples include:

 - Calculating points in a fractal.
 - Estimating Pi
 - Factoring primes.
 - Parsing HTML, JSON, etc. documents.
 - Processing text.
 - Running simulations.

 ## IO-Bound Tasks
An IO-bound task is a type of task that involves reading from or writing to a device, file, or socket connection.

The operations involve input and output (IO), and the speed of these operations is bound by the device, hard drive, or network connection. This is why these tasks are referred to as IO-bound.

CPUs are really fast. Modern CPUs, like a 4GHz, can execute 4 billion instructions per second, and you likely have more than one CPU in your system.

Doing IO is very slow compared to the speed of CPUs.

Interacting with devices, reading and writing files, and socket connections involve calling instructions in your operating system (the kernel), which will wait for the operation to complete. If this operation is the main focus for your CPU, such as executing in the main thread of your Python program, then your CPU is going to wait many milliseconds, or even many seconds, doing nothing.

That is potentially billions of operations that it is prevented from executing.

Examples of IO-bound tasks include:

 - Reading or writing a file from the hard drive.
 - Reading or writing to standard output, input, or error (stdin, stdout, stderr).
 - Printing a document.
 - Downloading or uploading a file.
 - Querying a server.
 - Querying a database.
 - Taking a photo or recording a video.
 - And so much more.

 Choose Python Concurrency API
Recall that the multiprocessing module provides process-based concurrency and the threading module provides thread-based concurrency within a process.

Generally, you should use process-based concurrency if you have a CPU-bound task and thread-based concurrency if you have an IO-bound task.

 * **CPU-Bound Tasks**: Use the “multiprocessing” module for process-based concurrency.
 * **IO-Bound Tasks**: Use the “threading” module for thread-based concurrency.

 Step 1.1 Choosing Between Threading and AsyncIO
If your tasks are mostly IO-bound, you have another decision point.

You must choose between using the “threading” module and using the “asyncio” module.

Recall that the threading module provides thread-based concurrency and the asyncio module provides coroutine-based concurrency within a thread.

Generally, you should use coroutine-based concurrency if you have many socket connections (or prefer asynchronous programming), and thread-based concurrency otherwise.

 - Many Socket-Connections: Use the “asyncio” module for coroutine-based concurrency.
 - Otherwise: Use the “threading” module for thread-based concurrency.


## Step 2: Many Ad Hoc Tasks vs One Complex Task?
The second step is to consider if you need to execute independent ad hoc tasks or a large complex task.

What we are thinking about at this decision point is whether you need to issue one or many ad hoc tasks that may benefit from a pool of reusable workers. Otherwise, whether you need a single task where a pool of reusable workers would be overkill.

Another way to think about it is whether you have one or a few different but complex tasks like monitors, schedulers or similar that might live for a long time, such as the duration of the program. These would not be ad hoc tasks, and may not benefit from a reusable pool of workers.

Shorter-lived and/or many ad hoc : Use a thread or process pool.
Longer-lived and/or complex tasks: Use the Thread or Process class.
In the case where you have chosen thread-based concurrency the choice is between a thread pool or using the Thread class.

In the case where you have chosen process-based concurrency, the choice is between a process pool or using the Process class.

Some additional considerations include:

 - Heterogeneous vs. Homogeneous Tasks: A pool is perhaps more appropriate for a diverse set of tasks (heterogeneous) whereas a Process/Thread class is appropriate for one type of task (homogeneous).
 - Reuse vs. Single Use: A pool is appropriate for reusing the basis of concurrency, e.g. reusing a thread or a process for many tasks, whereas a Process/Thread class is appropriate for a single use task, perhaps a long lived one.
 - Multiple Tasks vs. Single Task: A pool naturally supports many tasks, perhaps issued in many ways, whereas a Process/Thread class only supports one type of task, once configured or overridden.


To make this more concrete, let’s consider some examples:

 - A for-loop that calls a function many times with different arguments each iteration may be appropriate for a thread pool as workers can be reused for each task automatically as needed.
 - A background task that monitors a resource may be appropriate for a Thread/Process class as it is a long-running single task and may have a lot of complex and specialized functionality perhaps spread across many function calls.
 - A script that downloads many files would be appropriate for a pool of workers as each task is short in duration and there may be many more files than there are workers, allowing reuse of workers and queuing of tasks to complete.
 - A one-off task that maintains internal state and interacts with the main program may be appropriate for Thread/Process class as the class can be overridden to use instance variables for state and methods for modular functionality.

 ## Step 3: Pools vs Executors?
The third step is to consider the type of worker pool to use.

There are two main types, they are:

 - Pool: multiprocessing.pool.Pool and the port of the class to support threads in multiprocessing.pool.ThreadPool.
 - Executors: The concurrent.futures.Executor class and two sub-classes ThreadPoolExecutor and ProcessPoolExecutor.

Both provide pools of workers. The similarities are many and the differences are few and subtle.

For example, the similarities are:

 - Both have thread- and Process-based versions.
 - Both can execute ad hoc tasks.
 - Both support synchronous and asynchronous task execution.
 - Both provide support for checking the status and waiting for asynchronous tasks.
 - Both support callback functions for asynchronous tasks.


Choosing one over the other will not make a big impact on your program.

The main difference is in the API offered by each, specifically minor differences in focus or in how tasks are handled.

For example:

 - Executors provide the ability to cancel issued tasks, whereas the Pool does not.
 - Executors provide the ability to work with collections of heterogeneous tasks, whereas the Pool does not.
 - Executors do not provide the ability to forcefully terminate all tasks, whereas the Pool does.
 - Executors do not provide multiple parallel versions of the map() function, whereas the Pool does.
 - Executors provide the ability to access an exception raised in a task, whereas the Pool does not.
