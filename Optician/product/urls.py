from django.urls import path
from .views import product,product_detail
 
urlpatterns = [
    path('product/', product, name='product'),
    path('product-detail/', product_detail, name='product_detail'),
]