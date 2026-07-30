from abc import ABC, abstractmethod


class ABCExample(ABC):

    def __init__(self, value):  # ABC can have __init__ and attributes!!
        self.value = value

    @abstractmethod
    def do_something(self):
        pass


class InheritingClass1(ABCExample):
    def __init__(self, value):
        super().__init__(value)

    def do_something(self):
        print(f"ABC's attribute {self.value} can now be accessed with self")


class InheritingClass2(ABCExample):
    def __init__(self, value):
        super().__init__(value)

    def do_something(self): ...


inheriting_classes = [InheritingClass1("Hello"), InheritingClass2("World")]
for inheriting_class in inheriting_classes:
    inheriting_class.do_something()
