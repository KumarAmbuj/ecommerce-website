from django.contrib import admin

# Register your models here.

from .models import Owner,Product

admin.site.register(Owner)

admin.site.register(Product)