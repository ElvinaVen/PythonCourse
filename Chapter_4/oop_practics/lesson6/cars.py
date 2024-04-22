"""
Напишите класс Car, представляющий машину, имеющую следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime


class Car:
    def __init__(self, brand, model, years):
        self.brand = brand
        self.model = model
        self.years = years
        current_year = datetime.datetime.now().year
        if years > current_year:
            raise ValueError("Год выпуска не может быть больше текущего")


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car1 = Car('Toyota', 'Corolla', 2034)
# raises Exception('Эта машина еще не была выпущена')
