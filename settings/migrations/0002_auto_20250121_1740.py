# Generated by Django 3.2 on 2025-01-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='paid_by_sender_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='prepaid_postage_label_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
