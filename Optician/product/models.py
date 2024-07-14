from django.db import models

# Create your models here.

from Optician.utils.base import BaseModel

class Product(BaseModel):
    CART_TYPES = (
        (0, 'Choose'),
        (1, 'New Arrivals'),
        (2, 'Laptop'),
        (3, 'Smartphone'),
        (4, 'Tablet'),
    )

    title = models.CharField(max_length=100, verbose_name='Title of the cart', help_text='max 100 characters')
    image = models.ImageField(verbose_name='Image of the cart')
    change_image = models.ImageField(verbose_name='Change image of the cart')
    price = models.IntegerField(verbose_name='Price of the cart')
    brands = models.ManyToManyField('product.Brand', related_name='ProductBrand' )
    cart_type = models.IntegerField(choices=CART_TYPES, default=0, verbose_name='Type of the cart')
    is_published = models.BooleanField(default=False, verbose_name='Is published?')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'All Products'

    def __str__(self):
        return self.title      
    
class Brand(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title of the cart', help_text='max 100 characters')

    class Meta:
        verbose_name = 'Product brand'
        verbose_name_plural = 'All Products brands'

    def __str__(self):
        return self.title 