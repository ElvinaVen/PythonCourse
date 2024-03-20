from Category_class import Category
from Product_class import Product
from CategoryIter_class import CategoryIter
from utils import load_src_file

# Овощи Фрукты - это для подставления в name1 и name2

src_file = load_src_file()

category_list = []
total_list = []

for i in range(len(src_file)):
    print("\n---Задание 1---")
    category_object = Category.create_category_object(src_file[i])  # создаем экз.категории с пустым списком товаров
    for j in range(len(src_file[i]['products'])):
        product_object = Product.create_product_object(src_file[i]['products'][j])  # создаем экз.продукта
        products = category_object.add_product(product_object)  # добавляем экз.продукта в список товаров категории
        print(product_object)
    print(category_object)
    total_list = Category.create_category_total_list(category_object, category_list)  # формируем общий список экз-ров категории
print("-----------------------------------------------------------------")
print(f"Общий список всех категорий с продуктами:{total_list}")
print("-----------------------------------------------------------------")

print("\n---Задание 2---")
product_object1 = Product('Лимон', "Кислый", 25.0, 100)
product_object2 = Product('Ананас', "Сочный", 350.0, 10)
total_price = product_object1 + product_object2
print(f"Общая стоимость продуктов {total_price}")
# print("\n---Задание 2*---")
# category_object = Category.create_category_object(src_file[i])  # создаем экз.категории с пустым списком товаров
# for j in range(len(src_file[i]['products'])):
#     product_object = Product.create_product_object(src_file[i]['products'][j])  # создаем экз.продукта
#     products = category_object.add_product(product_object)  # добавляем экз.продукта в список товаров категории
#     # print(product_object)
# # print(category_object)
# total_list = Category.create_category_total_list(category_object,
#                                                  category_list)  # формируем общий список экз-ров категории
# # итератор, принимающий категорию
# my_cat_iter = CategoryIter(category_object)
# for item in my_cat_iter:
#     print(item)


for i in range(len(src_file)):
    print("\n---Задание 2*---")
    category_object = Category.create_category_object(src_file[i])  # создаем экз.категории с пустым списком товаров
    for j in range(len(src_file[i]['products'])):
        product_object = Product.create_product_object(src_file[i]['products'][j])  # создаем экз.продукта
        products = category_object.add_product(product_object)  # добавляем экз.продукта в список товаров категории
    print(f"Экземпляр категории с заполненным списком: {category_object}")
    my_cat_iter = CategoryIter(products)
    for item in my_cat_iter:
        print(item)
