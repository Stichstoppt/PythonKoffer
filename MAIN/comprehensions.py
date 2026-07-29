"""List"""


def basic_list_comprehensions():
    squares_comp = [i * i for i in range(1, 6)]

    # with a filter condition
    even_squares = [i * i for i in range(1, 11) if i % 2 == 0]

    # with a transformation and filter combined
    words = ["Hello", "world", "Python", "is", "great"]
    long_upper = [w.upper() for w in words if len(w) > 3]

    # conditional expression (ternary) inside comprehension
    labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]


""" Dict & Set """


def dict_and_set_comprehensions():
    # dict comprehension: {key_expr: val_expr for item in iterable}
    names = ["Alice", "Bob", "Charlie"]
    name_lengths = {name: len(name) for name in names}

    # inverting a dict
    original = {"a": 1, "b": 2, "c": 3}
    inverted = {v: k for k, v in original.items()}

    # dict comprehension with filter
    scores = {"Alice": 85, "Bob": 42, "Charlie": 91, "Dave": 67}
    passed = {name: score for name, score in scores.items() if score >= 60}

    # set comprehension: {expr for item in iterable}
    words = ["hello", "HELLO", "Hello", "world", "WORLD"]
    unique_lower = {w.lower() for w in words}

    # set comprehension for deduplication with transformation
    data = [1, -1, 2, -2, 3, -3, 3]
    abs_values = {abs(x) for x in data}


""" Bonus stuff """


def nested_comprehensions():
    # flatten a 2D list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]  # outer loop first, inner loop second

    # 2D construction: list of lists
    grid = [[col * row for col in range(1, 4)] for row in range(1, 4)]
    print(f" 2| grid:      {grid}")

    # Cartesian product with filter
    pairs = [(x, y) for x in range(4) for y in range(4) if x != y]
    print(f" 3| pairs x!=y: {pairs}")

    # transpose a matrix
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(f" 4| transposed: {transposed}")
