# Generated by Django 3.2 on 2024-11-10 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_model_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='model_type',
        ),
    ]