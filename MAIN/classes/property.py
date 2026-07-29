class PersonWithProperties:

    def __init__(self, name, age):
        self._name = name  # now protected
        self._age = age
        self._artist = False

    # ============================================================
    @property  # getter
    def age(self):
        """I'm the 'age' property"""
        return self._age

    @age.setter  # setter
    def age(self, value):
        """I'm the 'age' property setter"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # ============================================================

    def my_get_name(self) -> str:  # 'hand-made' getter and setter
        """name getter"""
        print(f" a|   name getter '{self._name}'")
        return self._name

    def my_set_name(self, value: str) -> None:
        """name setter"""
        print(f" b|   name setter '{self._name}', new '{value}'")
        self._name = value

    name = property(my_get_name, my_set_name, None, "my doc str")  # properties

    artist = property(
        lambda self: self._artist, lambda self, val: setattr(self, "_artist", val)
    )  # error for 'self._tag = val'


def show_properties():
    hp = PersonWithProperties(name="Hans-Peter K.", age=46)

    name = hp.name
    age = hp.age
    artist = hp.artist

    hp.name = "Horst S."
    hp.age = 57
    hp.artist = True

    try:
        hp.age = -1  # triggers ValueError from validation
    except ValueError as e:
        ...
