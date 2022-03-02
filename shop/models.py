from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
    owner_id=models.AutoField
    owner_username=models.CharField(max_length=30)
    owner_password=models.CharField(max_length=30)


class Category(models.Model):
    cat_id=models.BigAutoField(primary_key=True)
    cat_name=models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class Sub_Category(models.Model):
    sub_cat_id=models.BigAutoField(primary_key=True)
    sub_cat_name=models.CharField(max_length=100)
    sub_cat_image = models.ImageField(upload_to='shop/images/',default='')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_cat_name

class Product_Details(models.Model):
    prod_id=models.BigAutoField(primary_key=True)
    prod_name=models.CharField(max_length=100)
    prod_brand = models.CharField(max_length=100)
    prod_packet_size = models.CharField(max_length=100)
    prod_packet_type= models.CharField(max_length=100)
    prod_mrp = models.FloatField()
    prod_price = models.FloatField()
    prod_date = models.DateField(auto_now_add=True)
    prod_image=models.ImageField(upload_to='shop/images/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name


class Contactus(models.Model):
    sno=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    content = models.TextField()

    read =  models.IntegerField(default=0)


    def __str__(self):
        return  'msg from '+ self.name


class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400)
    landmark = models.CharField(max_length=200)
    mobileno = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    price =  models.CharField(max_length=100)
    eprice = models.CharField(max_length=100)
    cashmode=models.CharField(max_length=100,default='')
    order_date = models.DateField(auto_now_add=True)
    delivereddate = models.CharField(max_length=100,default='')

    packed = models.IntegerField(default=0)
    ondelivery = models.IntegerField(default=0)
    delivered = models.IntegerField(default=0)
    canceled = models.IntegerField(default=0)
    order_return = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order_Details(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    size = models.CharField(max_length=20)
    price1 = models.IntegerField()
    totalprice = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

class Return_Message(models.Model):
    msg_id = models.BigAutoField(primary_key=True)

    content = models.TextField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

class Coupon(models.Model):
    coupon_id = models.BigAutoField(primary_key=True)
    coupon_name = models.CharField(max_length=20)

    def __str__(self):
        return self.coupon_name

class Mobileno(models.Model):
    mobile_id = models.BigAutoField(primary_key=True)
    mobileno = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.mobileno











