def using_print():
    """Various printings."""  # Docstring for the function, hold the mouse on 'using_print'.

    print(" 1| simple 'print'")
    print(" 2| print without", end="")  # Print without line-feed.
    print(" new line")

    print(f" 3| expressions in f-strings: {2*7=}")  # Formatted string ('f').
    print(f" 4| {{ and }} in f-strings, e.g. for a set: {{ 1,{1+1} }}")

    print(" 5| escaped chars, e.g. \" ' \\ \\n")  # With special chars ('escaped').
    print(r" 6| as r-string (raw), i.e. as it is, e.g. '\n'")  # Raw string ('r').


def using_input():
    """Reads from the console."""

    name = input(" 1| Enter your name: ")  # Read a string into a (string) variable.
    print(f" 2| Hello '{name}'!")
