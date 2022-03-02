from django.db import models

# Create your models here.

class Owner(models.Model):
    owner_id=models.AutoField
    owner_username=models.CharField(max_length=30)
    owner_password=models.CharField(max_length=30)


class Product(models.Model):
    produc_id=models.AutoField
    product_name=models.CharField(max_length=30)
    product_desc=models.CharField(max_length=30)
    def __str__(self):
        return self.product_name