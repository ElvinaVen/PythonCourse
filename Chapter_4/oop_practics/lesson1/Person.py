from datetime import date


class Person:
    name: str
    age: int

    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Это {self.name}, ему {self.age}")


person = Person('Иван', 19)
person.display()

person1 = Person.from_birth_year('Николай', 2001)
person1.display()
