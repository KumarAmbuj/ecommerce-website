from django.contrib import admin

# Register your models here.

from .models import Owner
from .models import Category
from .models import Sub_Category
from .models import Product_Details
from .models import Contactus
from .models import Orders
from .models import Order_Details
from .models import Return_Message
from .models import Coupon
from .models import Mobileno



admin.site.register(Owner)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product_Details)
admin.site.register(Contactus)
admin.site.register(Orders)
admin.site.register(Order_Details)
admin.site.register(Return_Message)
admin.site.register(Coupon)
admin.site.register(Mobileno)




