# Generated by Django 3.2 on 2024-11-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20241107_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='storage_sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='ee_price_adjustment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='unlocked_price_adjustment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]