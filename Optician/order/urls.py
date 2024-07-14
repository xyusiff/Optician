from django.urls import path
from .views import shopping, checkout, wishlist
 
urlpatterns = [
    path('shopping/', shopping, name='shoping'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
]