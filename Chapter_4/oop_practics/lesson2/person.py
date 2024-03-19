"""
Напишите класс Person, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя и возраст человека
- display(self): метод, выводящий на экран имя и возраст человека
- from_birth_year(cls, name, birth_year): класс-метод, принимающий имя и год рождения человека и
возвращающий объект класса Person;
- is_adult(cls, age): статический метод, принимающий возраст человека и возвращающий True,
если он старше 18 лет, и False в противном случае
"""

from datetime import datetime


class Person:

    def __init__(self, name, age):
        """
        конструктор, принимающий имя и возраст человека
        :param name:
        :param age:
        """
        self.__name = name
        self.__age = age

    @property
    def person_name(self):
        return self.__name

    @property
    def person_age(self):
        return self.__age

    @person_name.setter
    def person_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            print("имя некорректно")

    @person_age.setter
    def person_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Возраст некорректный")

    def display(self):
        """
        метод, выводящий на экран имя и возраст человека
        :return:
        """
        print(f'{self.__name} is {self.__age} years old')

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """
        класс-метод, принимающий имя и год рождения человека и
        возвращающий объект класса Person;
        :param name:
        :param birth_year:
        :return:
        """
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        """
        статический метод, принимающий возраст человека и возвращающий True,
        если он старше 18 лет, и False в противном случае
        :param:
        :param age:
        :return:
        """
        if age >= 18:
            return True
        return False


# код для проверки 
person1 = Person("John", 28)
person1.__name = "Rokl776n"
print(person1.person_name)
print(person1.person_age)
person1.person_name = 3
person1.person_age = 6

print(person1.person_age)
print(person1.person_name)
person1.display()  # John is 28 years old

# person2 = Person.from_birth_year("Mike", 1995)
# person2.display()  # Mike is 26 years old
#
# print(Person.is_adult(20))  # True
# print(Person.is_adult(15))  # False
