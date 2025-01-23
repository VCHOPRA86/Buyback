# Generated by Django 3.2 on 2024-12-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_order_revised_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_response',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], max_length=10, null=True),
        ),
    ]
