# Generated by Django 3.2 on 2024-12-18 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revieworder', '0004_rename_network_cart_network_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='network_status',
            new_name='network',
        ),
    ]
