# Generated by Django 3.2 on 2024-11-16 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20241115_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand',
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]