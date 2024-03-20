import json


def load_src_file():
    """
    Ф-ия загрузки списка из json.
    :return: src_file - весь список категорий с описанием и товарами
    """
    with open('file_fruits.json', 'r', encoding='utf-8') as file:
        src_file = json.load(file)
    return src_file
