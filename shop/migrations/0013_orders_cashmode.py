# Generated by Django 3.2.4 on 2021-08-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_order_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cashmode',
            field=models.CharField(default='', max_length=100),
        ),
    ]
