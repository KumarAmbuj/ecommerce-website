# Generated by Django 3.2.4 on 2021-08-08 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0018_delete_mobileno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobileno',
            fields=[
                ('mobile_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mobileno', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]