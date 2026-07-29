######################
######for-loops#######
######################


def some_condition(x):
    return x == 3


# =============================================================================
# CORE MECHANICS & BUILT-IN ITERATORS
# =============================================================================
def core_mechanics():
    print("--- 1. Core Mechanics ---")

    # The standard range (start, stop, step) -> Note: 'stop' is exclusive
    for i in range(0, 10, 2):
        print(f"Range step 2: {i}")  # 0, 2, 4, 6, 8

    # Iterables (Strings, list)
    list = [1, 2, 3]
    for item in list:
        ...

    str = "abc"
    for char in str:
        ...

    # Reverse iteration using reversed()
    items = ["a", "b", "c"]
    for item in reversed(items):
        print(f"Reversed: {item}")  # c, b, a

    # Tracking index with enumerate(iterable, start=0)
    for index, value in enumerate(items, start=1):
        print(f"Index {index}: {value}")  # 1: a, 2: b, 3: c

    # Parallel iteration over multiple sequences via zip()
    # Note: zip() stops at the SHORTEST iterable unless you use itertools.zip_longest()
    names = ["Alice", "Bob"]
    ages = [25, 30, 35]  # 35 is ignored by standard zip
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")


# =============================================================================
# FOR-ELSE
# =============================================================================
def for_else_mechanic():
    print("\n--- 2. For-Else Loop ---")
    # THE RULE: The 'else' block executes IF AND ONLY IF the loop finishes
    # naturally without encountering a 'break' statement.

    # Case A: Loop runs to completion -> Else executes!
    for n in range(3):
        if n == 99:
            break
    else:
        print("Case A: No break encountered, else block triggers!")

    # Case B: Loop hits a break -> Else is SKIPPED!
    for n in range(3):
        if n == 1:
            break
    else:
        print("Case B: This will NEVER print because of the break.")


# =============================================================================
# COMPREHENSIONS & GENERATORS
# =============================================================================
def comprehensions_and_generators():
    print("\n--- 3. Comprehensions & Generators ---")

    # List Comprehension [expression for item in iterable if condition]
    squares = [x**2 for x in range(5) if x % 2 == 0]
    print(f"List Comp: {squares}")  # [0, 4, 16]

    # Dict Comprehension
    char_counts = {char: idx for idx, char in enumerate("ABC")}
    print(f"Dict Comp: {char_counts}")  # {'A': 0, 'B': 1, 'C': 2}

    # Generator Expression (Memory efficient, lazy evaluation)
    lazy_squares = (x**2 for x in range(1000000))
    print(f"Generator Type: {type(lazy_squares)}")  # <class 'generator'>
    print(f"First element: {next(lazy_squares)}")  # 0


# =============================================================================
# ITERTOOLS
# =============================================================================
import itertools


def advanced_itertools():
    print("\n--- 4. Itertools Patterns ---")

    # Infinite loop counter
    for count in itertools.count(start=10, step=5):
        if count > 20:
            break
        print(f"itertools.count: {count}")  # 10, 15, 20

    # Flattening nested loops / chaining iterables
    for item in itertools.chain([1, 2], ["a", "b"]):
        print(f"Chained: {item}")  # 1, 2, a, b

    # Nested Loops simplified (Cartesian Product) -> Replaces nested for loops
    # Equivalent to: for x in: for y in ['A','B']:
    for x, y in itertools.product([1, 2], ["A", "B"]):
        print(f"Product: {x}{y}")  # 1A, 1B, 2A, 2B
