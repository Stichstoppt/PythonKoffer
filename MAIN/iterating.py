"""
IMMER ITERATOR IMPLEMENTIEREN, ITERABLE RETURNT EIFNACH NUR ITERATOR-OBJEKT

All of these are 'Iterables': lists, tuples, strings, dicts, sets, ranges, etc.
They have an __iter__() method (implicitly called in for loop) that return an iterator object.
Python doesn’t require you to explicitly inherit from Iterable to be
considered one. If your object implements the required method (__iter__()),
Python says: "Looks like an iterable. Quacks like one. Good enough for me."

Funfact: iterator benutzt __getitem__ als fallback
Das ältere Sequenz-Protokoll (__getitem__ beginnend bei Index 0) existiert weiterhin als automatischer Fallback

Feature             Iterable            Iterator                    Generator
Implements          __iter__()          __iter__() + __next__()     Same as iterator (auto)
Works with iter()   yes                 yes (returns self)          yes
Works with next()   no(need iter first) yes                         yes
Reusable            yes                 no(consumed)                no(consumed)
Built-in Example    list, str, dict     iter(list), file obj        Generator function
Custom Example      Class w/ __iter__() Class w/ __next__()         Function w/ yield
"""

from collections.abc import Iterable, Iterator

# ===========================
# Iterator
# ===========================


class IteratorExample:  # wenn man von Iterator erbt, muss man __iter__ nicht explizit implementieren
    def __init__(self):
        self.data = [1, 2, 3, 4]
        self.index = 0

    # !!Returnt immer self!!
    def __iter__(self):
        return self

    # !!Raist für Abbruch die StopIteration Exception!!
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration  # SEHR SEHR WICHTIG: StopIteration signalisiert das Ende der Iteration
        value = self.data[self.index]
        self.index += 1
        return value


# ===========================
# Iterable
# ===========================


class IterableObj:
    # !!Returnt immer ein Iterator-Objekt!!
    def __iter__(self):
        return iter(
            [1, 2, 3, 4]
        )  # iter guckt nach __iter__ und __getitem__ in list und return Iterator


# ===========================
# for under the hood
# ===========================

it = IteratorExample()
for item in it:
    print(f"{item} ", end="")

# äquivalent zu:

it = IteratorExample()
while True:
    try:
        item = next(it)
        print(f"{item} ", end="")
    except StopIteration:
        break
