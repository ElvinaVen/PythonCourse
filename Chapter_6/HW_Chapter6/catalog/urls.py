from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, ProductUpdateView

from catalog.views import ProductDeleteView
from django.views.decorators.cache import cache_page



app_name = CatalogConfig.name

urlpatterns = [
    # path("", product_list, name="home"),
    # path("product/<int:pk>/", product_detail, name="product_detail"),

    path('', ProductListView.as_view(), name="products_list"),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
]
