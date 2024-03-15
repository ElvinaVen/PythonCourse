# import pytest
#
#
# @pytest.fixture
# def src_file():
#     return [{'name': 'Смартфоны',
#              'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
#              'products': [{'name': 'Samsung Galaxy C23 Ultra',
#                            'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
#                            'quantity': 5},
#                           {'name': 'Iphone 15', 'description': '512GB, Gray space',
#                            'price': 210000.0, 'quantity': 8}]},
#             {'name': 'Телевизоры',
#              'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
#              'products': [{'name': '55" QLED 4K',
#                            'description': 'Фоновая подсветка',
#                            'price': 123000.0,
#                            'quantity': 7}]}]

# def test_product_count(src_file):
#     products_list = create_products_list(src_file)
#     assert len(products_list) == 3
#
#
# def test_category_count(src_file):
#     category_list = create_category_list(src_file)
#     assert len(category_list) == 2
