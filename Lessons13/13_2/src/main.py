from DZ_13_OOP1.src.Category_class import Category
from DZ_13_OOP1.src.Product_class import Product
from DZ_13_OOP1.src.utils import load_src_file

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
    print(f"Экземпляр категории с заполненным списком: {category_object}")
    total_list = Category.create_category_total_list(category_object, category_list)  # формируем общий список экз-ров категории
    # print(category_object.products)
    print("\n---Задание 2---")
    print(category_object.products)
print("-----------------------------------------------------------------")
print(f"Общий список всех категорий с продуктами:{total_list}")
print("-----------------------------------------------------------------")

print("\n---Задание 3---")
category_name = "Фрукты"
new_product_object = Product.create_new_product_object('Киви', "Кислый", 90.0, 9)
print(f"Новый товар: {new_product_object}\n")
total_list = Category.add_new_product(new_product_object, total_list, category_name)
print(f"Общий список всех категорий с новым товаром:{total_list}")

print("\n---Задание 4---")
pr1 = Product(product_name="Киви", product_description="Кислый", product_price=90.0, product_quantity=9)
print(f"Товар: {pr1}, цена: {pr1.price}")  # Получение цены
pr1.price = 120.0  # Установка новой цены
print(f"Новая цена: {pr1.price}")  # Получение обновленной цены
