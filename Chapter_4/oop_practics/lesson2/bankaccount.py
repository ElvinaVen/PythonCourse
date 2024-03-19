"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): c

Для свойства balance используйте декоратор @property.
"""


class BankAccount:


    def __init__(self, balance):
        """
        конструктор, принимающий начальный баланс счета
        :param balance:
        """
        self.balance = balance  # свойство, которое возвращает текущий баланс счета

    @property
    def balance(self):

        return self._balance

    def deposit(self, amount):
        """
        метод, который позволяет внести деньги на счет
        :param amount:
        :return:
        """
        self.balance = self.balance + amount
        return self.balance


    def withdraw(self, amount):
        """
        метод, который позволяет снять деньги со счета
        :param amount:
        :return:
        """
        self.balance = self.balance - amount
        return self.balance


    def close(self):
        """
        метод, который позволяет снять деньги со счета
        :return:
        """
        self.balance = 0
        return self.balance

    @balance.setter
    def balance(self, value):
        self._balance = value


# код для проверки
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
