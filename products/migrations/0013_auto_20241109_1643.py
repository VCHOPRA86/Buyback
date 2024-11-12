# Generated by Django 3.2 on 2024-11-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20241109_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='condition_requirements',
        ),
        migrations.AddField(
            model_name='product',
            name='faulty_description',
            field=models.TextField(blank=True, help_text='Description for faulty condition', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='working_description',
            field=models.TextField(blank=True, help_text='Description for working condition', null=True),
        ),
    ]
