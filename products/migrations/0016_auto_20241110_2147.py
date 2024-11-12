# Generated by Django 3.2 on 2024-11-10 21:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20241109_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='faulty_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Description for faulty condition - Use <code>class="no-bullets"</code> in your <ul> tags to remove bullet points', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='working_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Description for working condition - Use <code>class="no-bullets"</code> in your <ul> tags to remove bullet points', null=True),
        ),
    ]
