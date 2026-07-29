from enum import Enum, auto, unique


@unique  # alle werte (hier 11, 22) müssen eindeutig sein, sonst wird eine Exception geworfen
class Drink(Enum):
    """unique enum values, i.e. no duplicates"""

    TEA = 11
    COFFEA = 22
    # WATER = 22 throws because of @unique


class ColorId(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    WHITE = 255
    EXTRA_WHITE = auto()  # increments from 255


class Defaults(Enum):
    URL = "https://www.google.com"
    Port = 8080
    User = "<USER>"
    Password = "<PASSWORD>"


def work_with_enums():
    tea = Drink.TEA

    coconut22 = Drink(22)  # access by value, throws if unknown
    coffea = Drink.COFFEA  # access by name, throws if unknown

    for drink in Drink:
        drink_name = drink.name
        drink_value = drink.value
