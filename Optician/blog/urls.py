from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('contact/', views.contact, name='contact'),
]