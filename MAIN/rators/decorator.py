"""
Decorator is syntactic sugar for a function which returns another function.
Before returning, it can add functionality before and after the inner function call.
"""


# =======================================================
# Decorator function, no input arguments, no return value
def decorator(some_f):
    def wrapper():
        print("DO SOMETHING BEFORE FUNC CALL")
        some_f()
        print("DO SOMETHING AFTER FUNC CALL")

    return wrapper


# Called with
@decorator
def f1():
    print(" c| -> in f")


# which is same as f1 = decorator(f1)!
# =======================================================


# =============================================================================
# DECORATOR FUNCTION, INPUT ARGUMENTS, RETURN VALUE AND PARAMETERIZED DECORATOR
from functools import partial


def do_repeat(_function_to_decorate=None, *, n=2):
    if callable(_function_to_decorate):

        @functools.wraps(_function_to_decorate)  # decorated function keeps meta data
        def wrapper_repeat(*args, **kwargs):  # function keeps args and kwargs

            #######################################
            # Actual functionality of the decorator
            value = None
            for _ in range(n):
                value = _function_to_decorate(*args, **kwargs)
            return value
            #######################################

        return wrapper_repeat  # case 1: no n provided
    else:
        return partial(do_repeat, n=n)  # case 2: n provided


# usage:
@do_repeat(n=3)
def p(alpha):
    return alpha * 2


@do_repeat
def q(beta):
    return beta * 2


# =======================================================


# ==============================================================================================
# CLASS DECORATOR
def add_repr_flexible_style():
    """class instance can be changed: e.g. functions can be added"""

    def add_repr(cls=None, *, fmt: str = "MyDict"):
        def decorator(cls):
            ###################################
            # New class method, add to cls
            def __repr__(self):
                return f"{fmt}:{self.__dict__}"

            cls.__repr__ = __repr__
            return cls
            ###################################

        return decorator(cls) if cls is not None else decorator

    @add_repr
    class Data1:
        def __init__(self, n: int):
            self.n = n

    @add_repr(fmt="Data2-Class")
    class Data2:
        def __init__(self, n: int):
            self.n = n


# ==============================================================================================


# ==============================================================================================
# THE COMPLICATED WAY FOR PARAMETERIZED DECORATOR (WITHOUT PARTIAL)
import functools


def do_repeat_complicated(_f=None, *, n=2):  # case 1 or 2 depends on _f==None
    def decorator_repeat(some_f):
        @functools.wraps(some_f)  # to not loose metadata of original function
        def wrapper_repeat(*args, **kwargs):  # for the function args
            value = None
            for _ in range(n):  # functionality of do_repeat
                value = some_f(*args, **kwargs)
            return value  # return value

        return wrapper_repeat

    # two cases: if _f is given, apply the decorator resulting in a wrapper,
    #            otherwise if n is given, then use the parameterized version being a decorator

    print(f" a| callable? {callable(_f)}, {_f=}")
    if callable(_f):  # case 1: function only
        return decorator_repeat(_f)
    else:
        return decorator_repeat  # case 2: do_repeat with parameters


# ==============================================================================================
