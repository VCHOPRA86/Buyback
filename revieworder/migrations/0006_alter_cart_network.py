# Generated by Django 3.2 on 2024-12-19 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revieworder', '0005_rename_network_status_cart_network'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='network',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
