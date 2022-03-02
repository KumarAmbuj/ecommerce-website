
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
def index(request):
    prod = Product.objects.all()
    print(prod)
    params = {'prods': prod}
    return render(request,'owner/index.html',params)


