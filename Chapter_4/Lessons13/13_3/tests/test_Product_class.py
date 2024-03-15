import pytest

from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import get_product_name, get_product_description, get_products_price, get_quantity


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


def test_initial_value_product(src_file):
    products_list = src_file[1]['products'][0]
    product_name = get_product_name(products_list)
    product_description = get_product_description(products_list)
    product_price = get_products_price(products_list)
    product_quantity = get_quantity(products_list)
    product_object = Product(product_name, product_description, product_price, product_quantity)

    assert product_object.product_name == '55" QLED 4K'
    assert product_object.product_description == 'Фоновая подсветка'
    assert product_object.__product_price == 123000.0
    assert product_object.product_quantity == 7
