# Generated by Django 3.2 on 2024-12-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0016_auto_20241219_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Awaiting Delivery', 'Awaiting Delivery'), ('Received', 'Received'), ('Processed', 'Processed'), ('Completed', 'Completed'), ('Expired', 'Expired'), ('Problem', 'Problem'), ('Quarantined', 'Quarantined'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled')], default='Awaiting Delivery', max_length=20),
        ),
    ]
