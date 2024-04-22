from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __init__(self):
        pass


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}, {self.__dict__.values()}'


class Product(MixinLog, Base):
    product_name: str
    product_description: str
    __product_price: float
    product_quantity: int  # количество в наличии

    def __init__(self, product_name, product_description, product_price, product_quantity):

        self.product_name = product_name
        self.product_description = product_description
        self.__product_price = product_price
        self.product_quantity = product_quantity

    # def __repr__(self):
    #     return f"{self.__class__.__name__} ('{self.product_name}' '{self.product_description}' '{self.__product_price}' '{self.product_quantity}')"

    # def __str__(self):
    #     return f'{self.product_name}, {self.__product_price} руб. Остаток: {self.product_quantity} шт.'

    @property
    def price(self):
        return self.__product_price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректная")
        else:
            self.__product_price = new_price
            print("Цена корректная")

    # @staticmethod
    # def my_decorator(func):
    #     def inner(**kwargs):
    #         result2 = {
    #             "name": kwargs['product_name'],
    #             "description": kwargs['product_description'],
    #             'price': kwargs['product_price'],
    #             'quantity': kwargs['product_quantity']
    #         }
    #         print(f"7) Создали новый экземпляр товара = {result2}")
    #         return result2
    #
    #     return inner

    @classmethod
    def create_product_object(cls, src_file):
        """
        Создаем экземпляры класса Product
        :param src_file
        :return: product_object
        """
        product_name = cls.get_product_name(src_file)
        product_description = cls.get_product_description(src_file)
        product_price = cls.get_product_price(src_file)
        product_quantity = cls.get_product_quantity(src_file)
        return cls(product_name, product_description, product_price, product_quantity)

    @classmethod
    def create_new_product_object(cls, product_name, product_description, product_price, product_quantity):
        """
        Создаем экземпляры класса Product
        :param product_quantity:
        :param product_price:
        :param product_description:
        :param product_name:
        :return: product_object
        """
        return cls(product_name, product_description, product_price, product_quantity)

    @staticmethod
    def get_product_name(src_file):
        """
        получаем наименование продукта для класса Products.
        :param src_file:
        :return:product_name
        """
        product_name = src_file['name']
        return product_name

    @staticmethod
    def get_product_description(src_file):
        """
        получаем описание продукта.
        :param src_file:
        :return:products_description
        """
        product_description = src_file['description']
        return product_description

    @staticmethod
    def get_product_price(src_file):
        """
        получаем цену продукта.
        :param src_file:
        :return:product_price
        """
        __product_price = src_file['price']
        return __product_price

    @staticmethod
    def get_product_quantity(src_file):
        """
        получаем количество на складе.
        :param src_file:
        :return:product_quantity
        """
        product_quantity = src_file['quantity']
        return product_quantity

    def __add__(self, other):
        if type(other) is Product:
            return float((self.__product_price * self.product_quantity) + (other.__product_price * other.product_quantity))
        else:
            raise TypeError("Нельзя складывать объекты разных классов.")


class Smartphone(Product, MixinLog):
    capacity: float
    model: str
    memory: int
    color: str

    def __init__(self, product_name, product_description, product_price, product_quantity, capacity, model, memory,
                 color):
        super().__init__(product_name, product_description, product_price, product_quantity)
        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color


class Grass(Product, MixinLog):
    manufacturer_country: str
    germination_period: str
    color: str

    def __init__(self, product_name, product_description, product_price, product_quantity, manufacturer_country,
                 germination_period, color):
        super().__init__(product_name, product_description, product_price, product_quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
