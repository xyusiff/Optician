# Generated by Django 5.0.6 on 2024-06-29 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comments_options_remove_blog_is_published'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]