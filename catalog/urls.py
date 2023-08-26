from django.urls import path
from catalog.views import home, contacts, product_details, products, category_products

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_details, name='product_details'),

]
