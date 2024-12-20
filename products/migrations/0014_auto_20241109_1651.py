# Generated by Django 3.2 on 2024-11-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20241109_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='faulty_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='working_description',
        ),
        migrations.AddField(
            model_name='product',
            name='condition_requirements',
            field=models.TextField(blank=True, help_text="Enter each requirement on a new line for working and faulty conditions. Use 'Working:' and 'Faulty:' to label sections.", null=True),
        ),
    ]
