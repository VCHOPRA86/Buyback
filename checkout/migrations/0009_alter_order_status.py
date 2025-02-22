# Generated by Django 3.2 on 2024-12-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_alter_order_postage_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Awaiting Delivery', 'Awaiting Delivery'), ('Received', 'Received'), ('Processed', 'Processed'), ('Completed', 'Completed'), ('Expired', 'Expired'), ('Problem', 'Problem'), ('Quarantined', 'Quarantined'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled')], default='Awaiting Delivery', max_length=20),
        ),
    ]
