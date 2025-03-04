from Category_class import Category
from Product_class import Product, Smartphone
from CategoryIter_class import CategoryIter
from utils import load_src_file


src_file = load_src_file()

print("\n---Задание 1---")
for i in range(len(src_file)):
     category_object = Category.create_category_object(src_file[i])  # создаем экз.категории с пустым списком товаров
     for j in range(len(src_file[i]['products'])):
         product_object = Product.create_product_object(src_file[i]['products'][j])  # создаем экз.продукта
         products = category_object.add_product(product_object)  # добавляем экз.продукта в список товаров категории
     product_object2 = Smartphone('POCO', "10MP камера", 35000.0, 1, 60, 'ZY22', 128, 'Yellow')

     products = category_object.add_product(product_object2)  # добавляем экз.продукта в список товаров категорииprint(f"Экземпляр категории с заполненным списком: {category_object}")
     my_cat_iter = CategoryIter(products)
     for item in my_cat_iter:
         print(item)

print("\n---Задание 2---")
print(category_object)
print(Category.average_price(category_object))