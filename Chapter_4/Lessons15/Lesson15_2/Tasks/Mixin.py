from abc import abstractmethod, ABC


class ShowMultBy(ABC):

    @abstractmethod
    def show_res_for(self, x):
        pass


class MultBy(ShowMultBy):
    """Класс, который использует миксин ShowMultBy."""

    def __init__(self, factor):
        self.factor = factor

    def multiply(self, x):
        return x * self.factor

    def show_res_for(self, x):
        print(f'Множитель: {self.factor}, Аргумент: {x},  Результат: {self.multiply(x)}')


f = MultBy(10)
f.show_res_for(20)
# Множитель: 10, Аргумент: 20, Результат: 200
sh = ShowMultBy()
# TypeError: Can't instantiate abstract class ShowMultBy with abstract method ...
