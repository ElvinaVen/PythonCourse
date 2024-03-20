class Category:
    category_name: str
    category_description: str
    __products: list  # это список товаров данной категории
    category_count = 0  # общее количество категорий
    product_count = 0  # общее количество уникальных продуктов

    def __init__(self, category_name, category_description, products):
        self.category_name = category_name
        self.category_description = category_description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.category_name}' '{self.category_description}' '{self.__products}')"

    def __len__(self, __products):
        product_count = 0
        for product in self.__products:
            product_count += product.product_quantity
        return product_count

    def __str__(self):
        return f'{self.category_name}, количество продуктов: {self.__len__(self.__products)} шт.'

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product.product_name}, {product.price} руб. Остаток: {product.product_quantity} шт.\n'
        return result

    @classmethod
    def create_category_object(cls, src_file):
        """
        создаем экз.категории с пустым списком товаров
        :param src_file
        :return: category_object
        """
        category_name = cls.get_category_name(src_file)
        category_description = cls.get_category_description(src_file)
        __products = []
        return cls(category_name, category_description, __products)

    @staticmethod
    def get_category_name(src_file):
        """
        получаем наименование категории
        :return:category_name
        """
        category_name = src_file['name']
        return category_name

    @staticmethod
    def get_category_description(src_file):
        """
        получаем описание категории
        :return:category_description
        """
        category_description = src_file['description']
        return category_description

    @staticmethod
    def add_new_product(new_product_object, total_list, category_name):
        """
        Создаем Общий список всех категорий с новым товаром
        :param new_product_object:
        :param total_list:
        :param category_name:
        :return:
        """
        for i, category_info in enumerate(total_list):
            if total_list[i].category_name == category_name:
                total_list[i].__products.append(new_product_object)
        return total_list

    def add_product(self, product_object):
        """
        добавляем экз.продукта в список товаров категории
        :param product_object:
        :return:
        """
        self.__products.append(product_object)
        return self.__products

    @staticmethod
    def create_category_total_list(category_object, category_list):
        """
        Сооздаем Общий список всех категорий с продуктами
        :param category_object:
        :param category_list:
        :return:
        """
        category_list.append(category_object)
        return category_list
