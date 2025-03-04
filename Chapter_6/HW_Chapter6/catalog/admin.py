from django.contrib import admin

# from Chapter_6.HW_Chapter6.catalog.models import Product, Category
from catalog.models import Product, Category, Version

# from C:Users.Эльвина.PycharmProjects.PythonCourse.Chapter_6.HW_Chapter6.catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ()


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name',)
    list_filter = ()
