"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.current_value = 0
        return self

    def __next__(self):
        if self.current_value < len(self.data):
            self.current_value += 1
            return self.current_value
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.data[item]


# код для проверки 
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print(my_list[1])  # 2

