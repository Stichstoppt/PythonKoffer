-classes
    -abc
    -cls keyword
    -dataclass
    -enum
    -property
    -für Klassen relevante sonstige annotations
    -dunda methods
-datastructures
    -dict.py
    -list.py
-threads
-decorator
-generator
-iterator
-lambda
-pattern_matching


# Threads (Kapitel 8 und 9)

- imports 
`
    import threading
    import concurrent.futures #threadpool, processpool
    import multiprocessing
`

- Initialize(!) thread (no starting yet)
- Threadpool
`
def some_function_which_should_be_executed_in_thread(msg, name, *, age, city): ...
thread_object = threading.Thread(
    target=some_function_which_should_be_executed_in_thread,
    name="thread_object",              # good practice for logging, debugging, inspecting running threads
    args=("Hello", "Alice"),           # Positional arguments
    kwargs={"age": 28, "city": "NYC"}  # Keyword arguments
)
load.start() # start thread
load.join()  # await result
`

- Daemon (Thread die nicht mehr gejoined werden muss)
`
thread_object = threading.Thread(target=some_function_which_should_be_executed_in_thread, daemon=true/false)
thread.start()
`

- Threadpool
`
with concurrent.futures.ThreadPoolExecutor(max_workers=anzahl_max_threads_gleichzeitig) as executor:
    /# startet task sofort, non-blocking, returns a Future
    future = executor.submit(some_function_which_should_be_executed_in_thread, "Hello", "Alice", age=28, city="NYC")
    result = future.result() # await result
`

`
with concurrent.futures.ThreadPoolExecutor(max_workers=anzahl_max_threads_gleichzeitig) as executor:
    def task(some_number): ...
    results = executor.map(task, (n/10.0 for n in range(1, 5))) # zweiter Parameter ist !Iterable!
    # !results ist ein Generator!
    try:
        # map stops at the _first_ exception (in submit order), so we never reach the rest
        for res in results:             # the ValueError surfaces here
            print("...")
        # also possbile: as_completed yields futures in completion order, not submission/creation order
        for future in concurrent.futures.as_completed(futures):
            print(f"{future.result()") # result aufrufen!!
    except ValueError as e:
        tprint(f" 6| caught: {e}")
`

- Processpool
`
def basic_process():
    p1 = multiprocessing.Process(name="ALICE", target=busy_worker, args=(0.3,))
    p1.start()
    p1.join()  # await
`
`
with ProcessPoolExecutor(max_workers=max_workers) as executor:
    executor.map(busy_worker, tasks)
`

- Weitere Themen
e_critical_regions.py
f_condition_variables.py
study_locks.py
study_producer_consumer.py
