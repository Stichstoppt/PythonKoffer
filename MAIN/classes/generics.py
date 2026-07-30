# T = TypeVar('T') # a generic type placeholder named 'T'

#####################
# GENERIC FUNCTION
def foo[T](x: T) -> T 
#####################


###############################################################
# GENERIC CLASS
class Box[T]:
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value

    def set(self, new_value: T) -> None:
        # with runtime safety
        if not isinstance(new_value, type(self.value)):
            raise TypeError("Wrong type")

        self.value = new_value

    def __repr__(self):
        return f"{self.value}[{type(self.value).__name__}]"
###############################################################


def construct_generic_typesafe_box():
    int_box = Box(42)  # int_box: Box[int] = Box(42)
    print(f" 1| {int_box=}")  # 42

    # str_box = Box[int]("hello")           # mypy: incompatible type
    str_box = Box[str]("hello")
    print(f" 2| {str_box=}")  # hello

    str_box.set("world")
    print(f" 3| {str_box=}")  # world

    # mypy: incompatible type => that is what we wanted!
    str_box.set(12.34)
    #############################

    print(f" 4| {str_box=} ???")  # remember: at runtime it works (if no type check)
