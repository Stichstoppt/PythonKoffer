class Person:  # inherits implicitly from 'object'
    def __init__(self, name):
        self.name = name
        print(f" a|   Person.init name='{self.name}', id={id(self)}")

    def introduce_myself(self):
        print(f" b|   --- Hello, I am {self.name} ---")

    def __del__(self):
        print(f" c|   Person.del name='{self.name}'")


class Employee(Person):  # with base class(es)
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print(f" d|   Employee.init name='{self.name}', id={id(self)}")

    def introduce_myself(self):
        super().introduce_myself()
        print(f" e|   --- and my salary is {self.salary} ---")

    def __del__(self):
        print(f" f|   Employee.del name='{self.name}'")
        super().__del__()


""" ISINSTANCE and ISSUBCLASS """


def check_types():
    peter = Person(name="Peter")
    mary = Employee(name="Mary", salary=1000)

    print(f" {isinstance(peter, Person)=}")
    print(f" {issubclass(Person, object)=}")
