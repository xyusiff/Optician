# Generated by Django 5.0.6 on 2024-07-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_brand_product_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='change_image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Change image of the cart'),
            preserve_default=False,
        ),
    ]
