"""
Async/await terminology:
- Suspendable function  A function that can be paused and resumed, i.e.,
                        an Async function.
- Async function        A function defined with 'async def', which returns
                        a coroutine when called.
- Suspension point      A point in a coroutine where it yields control to the
                        event loop (e.g. await something).
- Coroutine             An object created when you call an Async function
                        — it can be suspended and resumed.
- Awaitable             Any object you can await — typically a coroutine.

'Using' an Async function 'f':
- f                     A reference to the async function.
- f(42)                 Returns a coroutine object (nothing runs yet!).
- await f(42)           Runs the coroutine to the next await or completion.

'cooperative multitasking':
- A coroutine can be scheduled to run concurrently with other coroutines.
- The event loop is responsible for scheduling coroutines.
"""

import asyncio


async def login_async(name):
    print(f" 1| {name} is loging in ...")
    await asyncio.sleep(0.1)  # simulate a network call
    print(f" 2| {name} signed in.")
    return f"{name}_id"


async def coroutines_example():
    # ========================================
    # INIT COUROTINES, BUT NOTHING RUNS YET!!!
    coro_bob = login_async("Bob")
    coro_charly = login_async("Charly")
    # ========================================

    await asyncio.sleep(0.05)  # we wait a little bit, nothing runs

    # ============================================
    # NOW THEY START RUNNING!!!
    task_alice = asyncio.create_task(coro_bob)
    task_charly = asyncio.create_task(coro_charly)
    # ============================================

    await asyncio.sleep(0.05)

    # ==============================================================
    # NOW WE AWAIT RESULT!!!
    id_bob = await task_alice
    id_charly = await task_charly
    # ==============================================================


async def gathering_results_from_coroutines():
    # ==========================================================
    # INIT COUROTINES, BUT NOTHING RUNS YET!!!
    coro_bob = login_async("Bob")
    coro_charly = login_async("Charly")
    # ==========================================================

    await asyncio.sleep(0.05)  # we wait a little bit, nothing runs

    # ==========================================================
    # NOW THEY START RUNNING!!! wir warten bis alle fertig sind
    results = await asyncio.gather(coro_bob, coro_charly)
    id_bob, id_charly = results
    # ==========================================================

    ###############################################################

    # ==========================================================
    # INIT COUROTINES, BUT NOTHING RUNS YET!!!
    coro_bob = login_async("Bob")
    coro_charly = login_async("Charly")
    # ==========================================================

    await asyncio.sleep(0.05)  # we wait a little bit, nothing runs

    # ==========================================================
    # NOW THEY START RUNNING!!! wir starten alle, gehen auf das erste ein das fertig ist
    async for finished in asyncio.as_completed([coro_bob, coro_charly]):
        result = await finished
        print(result)
    # ==========================================================


async def task_group_gathering():
    async def boom(table, delay):
        try:
            await asyncio.sleep(delay)
            raise ValueError(f"query for '{table}' blew up!")
        except asyncio.CancelledError:
            raise

    async def exceptions_and_task_cancellation():
        try:
            async with asyncio.TaskGroup() as tg:
                tg.create_task(boom("people", 0.1))  # boom in 0.1
                tg.create_task(boom("projects", 0.1))  # boom in 0.1
                tg.create_task(
                    boom("orders", 0.3)
                )  # still running at boom, will be canceled
            ### WARTET HIER BIS ALLE TASKS FERTIG SIND, ODER BIS EIN EXCEPTION AUFTRITT!!!

        except* ValueError as eg:  # exception group, keyword 'except*' (since 3.11)
            print(f"Caught ValueError group with {len(eg.exceptions)} exceptions:")
            for e in eg.exceptions:
                print(e)


# =================================================
# VERY IMPORTANT: MUST START EVENT LOOP MANUALLY!!!
# =================================================
if __name__ == "__main__":
    asyncio.run(
        coroutines_example()
    )  # asyncio.run() creates an event loop, runs the coroutine, and closes the loop when done.
