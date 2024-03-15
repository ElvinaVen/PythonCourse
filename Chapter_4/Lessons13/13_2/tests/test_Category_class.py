import pytest

from DZ_13_OOP1.src import Category_class
# from DZ_13.2_OOP1.src.main import category_object
from DZ_13_OOP1.src.utils import get_category_name, get_category_description, get_category_products


@pytest.fixture
def src_file():
    return [{'name': 'Смартфоны',
             'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
             'products': [{'name': 'Samsung Galaxy C23 Ultra',
                           'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
                           'quantity': 5},
                          {'name': 'Iphone 15', 'description': '512GB, Gray space',
                           'price': 210000.0, 'quantity': 8}]},
            {'name': 'Телевизоры',
             'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
             'products': [{'name': '55" QLED 4K',
                           'description': 'Фоновая подсветка',
                           'price': 123000.0,
                           'quantity': 7}]}]


def test_initial_value_category(src_file):
    category_list = src_file[0]
    category_name = get_category_name(category_list)
    category_description = get_category_description(category_list)
    category_products = get_category_products(category_list)
    category_object = Category_class.Category(category_name, category_description, category_products)
    assert category_object.category_name == 'Смартфоны'
    assert category_object.category_description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert category_object.category_products == [{'name': 'Samsung Galaxy C23 Ultra',
                                                  'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
                                                  'quantity': 5},
                                                 {'name': 'Iphone 15', 'description': '512GB, Gray space',
                                                  'price': 210000.0, 'quantity': 8}]
    # assert Category_class.Category.category_count == 2
    # # assert category_object.product_count ==3
    # assert category_object.category_count == 2
# @pytest.fixture
# def test_quantity(src_file):
#     category_list = src_file[0]
#     category_name = get_category_name(category_list)
#     category_description = get_category_description(category_list)
#     category_products = get_category_products(category_list)
#     category_object = Category_class.Category(category_name, category_description, category_products)
#     assert category_object.category_count == 2