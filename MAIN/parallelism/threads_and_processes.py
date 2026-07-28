######################
#######Threads########
######################


def some_function_which_should_be_executed_in_thread(msg, name, *, age, city): ...


MAX_THREADS_AT_THE_SAME_TIME = 4

import threading  # Thread
import concurrent.futures  # threadpool, processpool
import multiprocessing  # Process

""" START AND JOIN (AND DAEMON) """


def start_join():
    thread_object = threading.Thread(
        target=some_function_which_should_be_executed_in_thread,
        name="thread_object",  # good practice for logging, debugging, inspecting running threads
        args=("Hello", "Alice"),  # Positional arguments
        kwargs={"age": 28, "city": "NYC"},  # Keyword arguments
        daemon=False,  # If thread is daemon, no join!
    )

    thread_object.start()  # start thread
    thread_object.join()  # await result


############################


""" THREADPOOL """


def threadpool():
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=MAX_THREADS_AT_THE_SAME_TIME
    ) as executor:
        """SIMPLE START AND AWAIT"""

        # starts task immediately, non-blocking
        future = executor.submit(
            some_function_which_should_be_executed_in_thread,
            "Hello",
            "Alice",
            age=28,
            city="NYC",
        )
        result = future.result()  # await result

        #########################################################

        """ .map / ACCESSING PROMISES AND RESULTS """

        def task(some_number): ...

        iterable = (n / 10.0 for n in range(1, 5))

        results = executor.map(task, iterable)  # zweiter Parameter ist !Iterable!

        # !results ist ein Generator!
        try:
            # map stops at the _first_ exception (in submit order), so we never reach the rest
            for res in results:  # the ValueError surfaces here
                print("...")

            # ALSO POSSBILE: as_completed yields futures in completion order, not submission/creation order
            futures = [executor.submit(task, n) for n in range(1, 5)]
            for future in concurrent.futures.as_completed(futures):
                print(f"{future.result()}")  # result aufrufen!!

        except ValueError as error:
            print(f"caught: {error}")


#########################


""" PROCESSPOOL """


def basic_process():
    p1 = multiprocessing.Process(
        name="PROCESS_FOO",
        target=some_function_which_should_be_executed_in_thread,
        args=("Hello", "Alice"),  # Positional arguments
        kwargs={"age": 28, "city": "NYC"},  # Keyword arguments
    )
    p1.start()  # start
    p1.join()  # await


def processpool():
    tasks = [1, 2, 3]
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=MAX_THREADS_AT_THE_SAME_TIME
    ) as executor:
        executor.map(basic_process, tasks)


""" LOCK/MUTEX - CRITICAL REGIONS"""

lock = threading.Lock()  # Init Lock/Mutex


def use_lock():
    def worker(*args, **kwargs):
        with lock:  # use contextmanager!!
            some_function_which_should_be_executed_in_thread(
                "Hello",
                "Alice",
                age=28,
                city="NYC",
            )

        # without contextmanager
        # lock.acquire()
        # current = ...
        # lock.release()

    thread_object = threading.Thread(
        target=some_function_which_should_be_executed_in_thread,
        name="thread_object",  # good practice for logging, debugging, inspecting running threads
        args=("Hello", "Alice"),  # Positional arguments
        kwargs={"age": 28, "city": "NYC"},  # Keyword arguments
        daemon=False,  # If thread is daemon, no join!
    )

    thread_object.start()
    thread_object.join()


#############################

""" CONDITION VARIABLE """

import time


def use_condition_variables():
    ###### IRRELEVANT ########
    def sign_in(budget: float):
        time.sleep(budget)

    load_image = sign_in
    ##########################

    signal = threading.Condition()
    ready = False  # shared state the receiver checks

    def sender():
        nonlocal ready
        sign_in(budget=0.05)  # even if we fire 'first', no signal is lost
        # HIER WICHTIG
        with signal:
            ready = True  # set the state ...
            signal.notify()
        ################

    def receiver():
        load_image(budget=0.05)  # modify to see predicate guard in action
        # HIER WICHTIG
        with signal:
            while not ready:  # while because of spurious makeups;
                signal.wait()  # if 'ready' is already set, we never wait -> order-independent
        ################

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(receiver)
        executor.submit(sender)
