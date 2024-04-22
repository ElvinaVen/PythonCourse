"""
Для класса Employee, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        # else:
            # raise TypeError('Unsupported operand type(s) for +: {} and {}'.format(type(self), type(other)))
        elif isinstance(other, int):
            return self.pay + other
        else:
            raise TypeError('Unsupported operand type(s) for +: {} and {}'.format(type(self), type(other)))


class Client:

    def __init__(self, pay):
        self.pay = pay

    # def __add__(self):
    #     return self.pay


class Developer(Employee):

    def __init__(self, pay):
        super().__init__(pay)


class Manager(Employee):

    def __init__(self, pay):
        super().__init__(pay)


# код для проверки
# users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]
users = [Employee(10000), Developer(20000), Manager(30000), Client(100000)]

total_salary = 0
for user in users:
    # print(user.pay)
    total_salary = user + total_salary


print(total_salary)
# Вывод: 150000
