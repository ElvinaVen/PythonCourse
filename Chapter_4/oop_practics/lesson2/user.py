"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в
False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:

    def __init__(self, name, password):
        """
        конструктор, принимающий имя пользователя и пароль
        :param name: свойство, которое возвращает имя пользователя
        :param password:  свойство, которое позволяет установить или изменить пароль пользователя
        """
        self.name = name
        self.password = password
        # self.is_admin = is_admin
        self._is_admin = False
        self._is_logged_in = False

    @property
    def name_func(self):
        return self.name

    @property
    def password_func(self):
        return self.password

    @name_func.setter
    def name_func(self, name):
        self.name = name


    @password_func.setter
    def password_func(self, password):
        self.password = password


    def login(self, password):
        """
        метод, который проверяет, соответствует ли введенный пароль паролю пользователя
        :param password:
        :return:
        """
        if password == self.password:
            self._is_logged_in = True
            return True
        return False

    def logout(self):
        """
        метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии,
         что пользователь залогинен)
        :return:
        """
        if self._is_logged_in:
            self._is_logged_in = False

    @property
    def is_admin(self):
        return self._is_admin


# код для проверки
user1 = User("Alice", "qwerty")
print(user1.name_func)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False
#
user1.password = "newpassword"
print(user1.password_func)  # newpassword
#
user1._is_admin = True
print(user1.is_admin)  # True
#
user1.login("newpassword")  # True
print(user1.login("newpassword"))
user1.logout()
