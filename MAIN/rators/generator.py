"""
Concept                 How You Write It            What It Is                  What It Returns / Does

Generator Function      def + yield inside          function producing          Does not run yet, returns
                                                    a generator iterator        generator iterator
Generator Iterator      Result of calling a         The actual iterator         Provides values when
                        generator function          object                      next() is called
Generator Expression    (expr for item in iterable) inline, lazy generator      Returns a generator iterator
                                                    producing values on demand  immediately
Generator (informal)    Often used to refer to      Usually means
                        any of the above            generator iterator
"""

"""
Reusing generator iterators is not possible. Making a new generator iterator out of a
generator function and then "reusing" it is possible. 
"""


# ========================
# define and use generator
# ========================
from collections.abc import Iterator


# generator function!
def generate_data(
    start_value, lower_limit, upper_limit
) -> Iterator[int]:  # returns iterator
    yield start_value
    for i in range(lower_limit, upper_limit + 1):
        yield i


# generator iterator!
items_gen = generate_data(7, 1, 20)
for n in items_gen:
    print(n)


# ========================
# generator expression
# ========================
def show_generator_expressions():
    gen_squares = (
        i * i for i in range(1, 5)
    )  # generator expression with () not [] like list


# ========================
# yield from
# ========================
def introducing_yield_from():
    def f_gen1():
        return (i * i * i for i in range(1, 3))  # 1, 8

    # generator function that yields from another generator
    def gen_from(g1, g2):
        yield from g1
