class example:
    class_variable = "I am a class variable"

    # returns a new instance of the class
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of the class...")
        instance = super().__new__(cls)
        return instance

    # returns none, initializes the instance
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        return f"This is a class method. Class variable: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "This is a static method. It does not have access to class or instance variables."


example_instance = example("I am an instance variable")

"""
    Unterschied zwischen Klassenobjekt(cls) und Objekt einer Klasse:
    - Klassenobjekt(cls) ist die Klasse als Objekt im Speicher, kann Funktionen und Attribute haben
    - Objekt einer Klasse ist aus Klasse erzeugtes Objekt!
"""
"""
    Wann @classmethod und wann @staticmethod?
    - @classmethod: wenn man Zugriff auf die Klasse selbst benötigt -> vorallem Factories
    - @staticmethod: Funktion die keinen Zugriff auf die Klasse oder Instanz benötigt, nur kontextuell passt
"""
