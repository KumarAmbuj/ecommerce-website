# Generated by Django 3.2.4 on 2021-08-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_coupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobileno',
            fields=[
                ('mobile_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mobileno', models.CharField(max_length=20)),
            ],
        ),
    ]