class LoggingDict:
    """the logging dict class"""

    def __init__(self):  # skip all other ways to initialize
        self.log_dict = {}

    def __getitem__(self, key):
        print(f" a|   getitem, key={key}")
        return self.log_dict[key]

    def __setitem__(self, key, value):  # also __delitem__
        print(f" b|   setitem, key={key}, value={value}")
        self.log_dict[key] = value

    def __delitem__(self, key):
        print(f" c|   delitem, key={key}")
        del self.log_dict[key]

    def __len__(self):
        print(" d|   len")
        return self.log_dict.__len__()

    def __iter__(self):
        print(" !!iter!!")
        return iter(self.log_dict)

    def __contains__(self, key):
        print(" e|   in")
        return key in self.log_dict

    def __repr__(self):
        return f"({self.log_dict})"

    def items(self):  # same for keys(), values()
        """forward items"""
        return self.log_dict.items()

    def get(self, key, default=None):
        """forward get"""
        return self.log_dict.get(key, default)


def test_logging_dicts():
    """test our class"""

    ld = LoggingDict()
    print(f" 1| {ld=}")

    ld[1] = "one"
    ld["two"] = 2
    ld[(1, 2)] = 3
    print(f" 2| ld={ld}, len={len(ld)}, {ld[1]=}, {ld.get(2,-1)=}")

    print(f" 3| {1 in ld=}, {2 in ld=}")

    del ld[(1, 2)]
    print(f" 4| ld={ld}")

    print(" 5| keys:", end="")
    for key in ld.log_dict:  # same as keys()
        print(f" {key=}", end="")
    print()

    print(" 6| keys:", end="")
    for key in ld:  # calls __iter__
        print(f" {key=}", end="")
    print()

    print(" 7| items:", end="")
    for k, v in ld.items():
        print(f" ({k},{v})", end="")
    print()

    print(" 8| enumerate:", end="")
    for i, item in enumerate(ld.items()):  # no, item
        print(f" {i}|{item}", end="")
    print()


"""
Topic: Equality and hashing
"""


class Point:
    """a simple 2D point with equality and hashing"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def test_equality_and_hashing():
    """equality and hashing for custom objects"""

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    print(f" 1| {p1=}, {p2=}, {p3=}")
    print(f" 2| {(p1 == p2)=}, {(p1 == p3)=}, {(p1 is p2)=}")
    print(f" 3| {hash(p1)=}, {hash(p2)=}, {(hash(p1) == hash(p2))=}")

    point_set = {p1, p2, p3}  # p1 and p2 are equal, so set has 2 elements
    print(f" 4| {point_set=}, {len(point_set)=}")

    point_dict = {p1: "origin-ish", p3: "further out"}
    print(f" 5| {point_dict=}, {point_dict[p2]=}")

    # p1.x=10  # break the dict
    print(f" 6| {hash(p1)=} {point_dict=}, {point_dict[p1]=}")


"""
Topic: Arithmetic operators
"""


class Vec2:
    """a simple 2D vector with arithmetic operators"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):  # right-side multiplication, called for: scalar * vec
        return self.__mul__(scalar)  # there are more reversed-side-op r<something>

    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"


def test_arithmetic_operators():
    """arithmetic operators for custom objects"""

    v1 = Vec2(1.0, 2.0)
    v2 = Vec2(3.0, 4.0)

    print(f" 1| {v1=}, {v2=}")
    print(f" 2| {(v1 + v2)=}")
    print(f" 3| {(v2 - v1)=}")
    print(f" 4| {(v1 * 3)=}")
    print(f" 5| {(2 * v2)=}")  # calls __rmul__


"""
Topic: Comparison operators with total_ordering
"""

from functools import total_ordering


@total_ordering
class Student:
    """student with name and grade, ordered by grade"""

    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return isinstance(other, Student) and self.grade == other.grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade

    def __repr__(self):
        return f"Student({self.name!r}, {self.grade})"


def test_total_ordering():
    """all six comparisons from just __eq__ and __lt__"""

    alice = Student("Alice", 1.3)
    bob = Student("Bob", 2.7)
    carol = Student("Carol", 1.3)

    print(f" 1| {alice=}, {bob=}, {carol=}")
    print(f" 2| {(alice == carol)=}")  # __eq__
    print(f" 3| {(alice < bob)=}")  # __lt__
    print(f" 4| {(bob > alice)=}")  # filled in by @total_ordering
    print(f" 5| {(alice <= carol)=}")  # filled in by @total_ordering
    print(f" 6| {(bob >= alice)=}")  # filled in by @total_ordering
    print(f" 7| {(alice != bob)=}")  # filled in by @total_ordering

    students = [bob, alice, carol]
    print(f" 8| sorted: {sorted(students)}")
