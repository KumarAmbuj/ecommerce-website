
from django.shortcuts import render , redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from datetime import datetime


from django.core.files.storage import FileSystemStorage

from .models import Category
from .models import Sub_Category
from .models import Product_Details
from .models import Orders
from .models import Order_Details
from .models import Return_Message
from .models import Coupon
from .models import Mobileno
from django.db import models
import re
import json
import datetime

from django.contrib.auth import authenticate, login , logout

from .models import Contactus
from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.
def index(request):
    category=Category.objects.all()
    topcategories=Sub_Category.objects.all()[:6]
    newarrival=Sub_Category.objects.all().order_by('-sub_cat_id')[:6]
    shopfast = Product_Details.objects.filter(category_id=3)[:6]

    cats1 = Category.objects.filter(cat_name='Grains')
    cat1 = None
    for x in cats1:
        cat1=x

    grocery=[]
    if cat1!=None:

        grocery = Sub_Category.objects.filter(category_id = cat1.cat_id)[:6]



    cats2 = Category.objects.filter(cat_name='Fruits')
    cat2 = None
    for x in cats2:
        cat2 = x

    fruits=[]
    if cat2 != None:
        fruits = Sub_Category.objects.filter(category_id=cat2.cat_id)[:6]

    cats3 = Category.objects.filter(cat_name='Vegetables')
    cat3 = None
    for x in cats3:
        cat3 = x

    vegetables = []
    if cat3 != None:
        vegetables = Sub_Category.objects.filter(category_id=cat3.cat_id)[:6]

    params = {'category': category, 'topcategories': topcategories, 'newarrival': newarrival, 'shopfast': shopfast,
              'grocery': grocery, 'fruits': fruits,'vegetables':vegetables}
    return render(request, 'shop/index.html', params)




def productview(request,id):
    category = Category.objects.all()

    prod=Product_Details.objects.filter(subcategory_id=id)

    subcat= Sub_Category.objects.get(sub_cat_id=id)
    cat = Category.objects.get(cat_id=subcat.category_id)


    params={'prods':prod,'category':category,'subcat':subcat,'cat':cat}
    return render(request, 'shop/productview.html',params)

# def index2(request):
#     category=Category.objects.all()
#     params={'category':category}
#     return render(request,'shop/index2.html',params)




def signup(request):

    if request.method == 'POST':
        
        
        usersname=request.POST['usersname']
        userfirstname=request.POST['userfirstname']
        userlastname=request.POST['userlastname']
        useremail=request.POST['useremail']
        usermobileno=request.POST['usermobileno']
        userpassword=request.POST['userpassword']
        userconfirmpassword=request.POST['userconfirmpassword']

        

        if len(usersname)<5:
            messages.error(request, "User name must be greater than 4 character and contains alphabet,number and special character ")
            return redirect('index')
        if User.objects.filter(username=usersname).exists():
            messages.error(request, "this username has already taken try other one")
            return redirect('index')

        if len(userfirstname)<3:
            messages.error(request, "name must be greater than 2 character")
            return redirect('index')

        if not userfirstname.isalpha():
            messages.error(request, "name must contain alphabets only")
            return redirect('index')





        if User.objects.filter(email=useremail).exists():
            messages.error(request, "this email  already exists")
            return redirect('index')




        def isValid(s):
            Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
            return Pattern.match(s)



        if (not isValid(usermobileno)):
            messages.error(request, "invalid mobile number")
            return redirect('index')


        if userpassword != userconfirmpassword:
            messages.error(request, "password and confirm password must be same")
            return redirect('index')





        myuser = User.objects.create_user(usersname,useremail,userpassword)

        myuser.first_name=userfirstname
        myuser.last_name=userlastname
        myuser.mobileno=usermobileno



        myuser.save()
        messages.success(request, "Your Acoount has been created successfully")


        
        return redirect('index')

    


    else:
        return redirect('index')




# def productview2(request,id):
#     prod=Product_Details.objects.filter(subcategory_id=id)
#
#     params={'prods':prod}
#     return render(request, 'shop/productview2.html',params)


def search(request):
    category = Category.objects.all()
    query = request.GET['query']
    if len(query)>78 or len(query)<=2:
        allPosts=[]
    else:
        allPostsname = Product_Details.objects.filter(prod_name__icontains=query)
        allPostsbrand = Product_Details.objects.filter(prod_brand__icontains=query)

        allPosts = allPostsname.union(allPostsbrand)
    
    

    
    params = {'allPosts': allPosts , 'category':category, 'query':query}
    return render(request,'shop/search.html', params)
    #return HttpResponse('search')


def checkout(request):
    category = Category.objects.all()
    flag=False
    value=0
    params = {'category': category , 'flag':flag , 'value':value}
    coupons = Coupon.objects.all()
    coupon=None

    for x in coupons:
        coupon=x

    if coupon ==None:
        messages.error(request, "Sorry currently no coupon available")
        return render(request, 'shop/checkout.html', params)

    if request.method == 'POST':

        name = request.POST['promocode']

        if coupon.coupon_name == name:

            flag = True
            value = int(name[3:])

            params = {'category': category, 'flag': flag, 'value': value}
            messages.success(request, "Promocode applied successfully")
            return render(request, 'shop/checkout.html', params)
        else:
            falg = False
            print(value)
            print(type(value))
            messages.error(request, "Invalid promocode")
            return render(request, 'shop/checkout.html', params)

    return render(request, 'shop/checkout.html', params)








def tracker(request):
    return HttpResponse('tracker')

def aboutus(request):
    return HttpResponse('aboutus')

def contactus(request):

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['mobileno']
        email = request.POST['email']
        city = request.POST['city']
        content = request.POST['content']


        if len(name)<2 or len(email)<3 or len(phone)<10 or len(city)<3 or len(content)<4:
            messages.error(request, "Please fill out correctly")
        else:
            contact = Contactus(name=name, phone=phone, email=email, city=city, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully")






    category = Category.objects.all()
    params = {'category': category}
    return render(request, 'shop/contactus.html', params)

def shophome(request):
    category=Category.objects.all()
    topcategories=Sub_Category.objects.all()[:6]
    newarrival=Sub_Category.objects.all().order_by('-sub_cat_id')[:6]
    shopfast = Product_Details.objects.filter(category_id=3)[:6]

    cats1 = Category.objects.filter(cat_name='Grains')
    cat1 = None
    for x in cats1:
        cat1 = x

    grocery = []
    if cat1 != None:
        grocery = Sub_Category.objects.filter(category_id=cat1.cat_id)[:6]

    cats2 = Category.objects.filter(cat_name='Fruits')
    cat2 = None
    for x in cats2:
        cat2 = x

    fruits = []
    if cat2 != None:
        fruits = Sub_Category.objects.filter(category_id=cat2.cat_id)[:6]

    cats3 = Category.objects.filter(cat_name='Vegetables')
    cat3 = None
    for x in cats3:
        cat3 = x

    vegetables = []
    if cat3 != None:
        vegetables = Sub_Category.objects.filter(category_id=cat3.cat_id)[:6]

    params = {'category': category, 'topcategories': topcategories, 'newarrival': newarrival, 'shopfast': shopfast,
              'grocery': grocery, 'fruits': fruits, 'vegetables': vegetables}



    return render(request,'shop/shophome.html',params)


def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "User Successfully Logged in")
            return redirect('shophome')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('index')
    else:
        return redirect('index')


def handlelogout(request):
    logout(request)
    messages.success(request, "successfully Logged Out")
    return redirect('index')


def bottomsearch(request):
    category = Category.objects.all()

    if request.method=="POST":
        query = request.POST['query']
        if len(query) > 78 or len(query) <= 2:
            allPosts = []
        else:
            allPostsname = Product_Details.objects.filter(prod_name__icontains=query)
            allPostsbrand = Product_Details.objects.filter(prod_brand__icontains=query)

            allPosts = allPostsname.union(allPostsbrand)

        params = {'allPosts': allPosts, 'category': category, 'query': query}
        return render(request, 'shop/bottomsearch.html', params)

    else:
        params = {'category': category}
        return render(request, 'shop/bottomsearch.html', params)


def placeorder(request):
    orderid=0
    if request.method == "POST":
        #username= request.POST['username']
        itemJson = request.POST['itemJson']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        landmark = request.POST['landmark']
        mobileno = request.POST['mobileno']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        price = request.POST['price']
        eprice = request.POST['eprice']

        data = json.loads(itemJson)


        if len(data)==0:
            messages.error(request, 'Your cart is empty!!! Please add some product in cart')
            category = Category.objects.all()
            params = {'category': category}
            return redirect('checkout')


        user = None
        if request.user.is_authenticated :
            user = request.user

        order = Orders(item_json=itemJson,first_name=fname,last_name=lname,address1=address1,address2=address2,landmark=landmark,mobileno=mobileno,city=city,state=state,pincode=pincode,price=price,eprice=eprice,user=user)
        order.save()
        for x in data:
            name=data[x][1]
            brand=data[x][2]
            qty=data[x][0]
            size=data[x][3]
            size=size.strip()
            price1=data[x][4]
            tprice=data[x][5]
            ods=Order_Details(name=name,brand=brand,quantity=qty,size=size,price1=price1,totalprice=tprice,user=user,order=order)

            ods.save()

        category = Category.objects.all()
        orderid=order.order_id
        params = {'category': category,'orderid':orderid}
        return render(request, 'shop/payment.html', params)

    category = Category.objects.all()
    params = {'category': category, 'orderid':orderid}
    return render(request, 'shop/payment.html', params)


def payment(request):

    category = Category.objects.all()
    params = {'category': category}
    if request.method == 'POST':
        payment = request.POST['payment']
        orderid = request.POST['orderid']
        if payment  == 'cod':

            obj = Orders.objects.get(pk=orderid)
            obj.cashmode = 'COD'
            obj.save()
            messages.success(request, 'Your record has been recorded keep shopping')
            return redirect('shophome')


        elif payment  == 'paytm':
            obj = Orders.objects.get(pk=orderid)
            obj.cashmode = 'Paytm'
            obj.save()
            messages.success(request, 'Your record has been recorded keep shopping')
            pass
        elif payment  == 'rupay':
            obj = Orders.objects.get(pk=orderid)
            obj.cashmode = 'RuPay'
            obj.save()
            messages.success(request, 'Your record has been recorded keep shopping')
            pass


    return render(request, 'shop/payment.html',params)

def userorder(request):
    category = Category.objects.all()
    params = {'category': category}
    return render(request, 'shop/userorder.html', params)

def handleuserorder(request):
    query = request.GET['orderquery']
    userid=0
    if request.user.is_authenticated:
        userid = request.user.id

    orders = Orders.objects.filter(order_id=query)

    if len(orders)==0:
        messages.error(request, 'INVALID ORDER ID enter correct order id')
        category = Category.objects.all()
        params = {'category': category}
        return render(request, 'shop/userorder.html', params)

    order=None
    for x in orders:
        order =x

    list=[]
    if order.user.id == userid:
        prod=Order_Details.objects.filter(order_id = query)

        print(type(prod))



        list.append(order)
        list.append(prod)

        category = Category.objects.all()
        params = {'category': category,'prods':list}
        flag =False
        if order.delivered ==1:
            date = datetime.datetime.strptime(order.delivereddate, '%Y-%m-%d %H:%M:%S.%f')
            z = datetime.datetime.now()


            delta = (z-date).days

            if delta<=10:
                flag=True

        category = Category.objects.all()
        params = {'category': category, 'prods': list, 'flag':flag}
        return render(request, 'shop/userorder.html', params)
    else:
        messages.error(request, 'INVALID ORDER ID')
        category = Category.objects.all()
        params = {'category': category}
        return render(request, 'shop/userorder.html', params)

def handleuserordercancelled(request,id):

    obj = Orders.objects.get(pk=id)
    obj.canceled = 1
    obj.save()
    return redirect('userorder')


def handleuserorderreturned(request, id):
    category = Category.objects.all()
    params = {'category': category,'id':id}

    if request.method == 'POST':
        print('hello')

        content = request.POST['reason']
        order = Orders.objects.filter(order_id=id).first()


        if len(content)<4:
            messages.error(request, "Please fill out valid reason")
        else:
            msg = Return_Message(content=content, order=order)
            msg.save()

            obj = Orders.objects.get(pk=id)
            obj.order_return = 1
            obj.save()

            messages.success(request, "Your request has been sent successfully, wait for company's reply")
            return redirect('userorder')




    return render(request, 'shop/handleuserorderreturned.html', params)


def useraccount(request):
    category = Category.objects.all()

    user = None
    if request.user.is_authenticated:
        user = request.user



    params = {'category': category,'user':user}

    return render(request, 'shop/useraccount.html', params)













def ownerhome(request):
    user = None
    flag=False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag=True
    params={'flag':flag}
    return render(request, 'shop/ownerhome.html',params)

def addcategory(request):
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True
    if request.method == 'POST':
        category = request.POST['category']

        cat = Category(cat_name=category)
        cat.save()
        messages.success(request, "1 category is added successfully")


    params={'flag':flag}
    return render(request, 'shop/addcategory.html',params)

def addsubcategory(request):
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    category = Category.objects.all()
    if request.method == 'POST':
        subcat = request.POST['subcategory']
        upload = request.FILES['img']
        id = request.POST['category']

        cat =  Category.objects.filter(cat_id = id).first()

        subcat = Sub_Category(sub_cat_name=subcat,sub_cat_image=upload,category=cat)
        subcat.save()

        messages.success(request, "1 subcategory is added successfully")

    params={'category':category,'flag':flag}

    return render(request, 'shop/addsubcategory.html',params)

def addproductdetails(request):
    category = Category.objects.all()
    subcategory = Sub_Category.objects.all()
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    if request.method == 'POST':
        prodname = request.POST['prodname']
        prodbrand = request.POST['prodbrand']
        prodpacketsize = request.POST['prodpacketsize']
        prodpackettype = request.POST['prodpackettype']
        prodmrp = request.POST['prodmrp']
        prodprice = request.POST['prodprice']

        upload = request.FILES['img']
        catid = request.POST['category']
        subcatid = request.POST['subcategory']



        cat =  Category.objects.filter(cat_id = catid).first()
        subcat = Sub_Category.objects.filter(sub_cat_id=subcatid).first()

        prod = Product_Details(prod_name=prodname,prod_brand=prodbrand,prod_packet_size=prodpacketsize,prod_packet_type=prodpackettype,prod_mrp=prodmrp,prod_price=prodprice,prod_image=upload,category=cat,subcategory=subcat)
        prod.save()

        messages.success(request, "1 product is added successfully")

        params = {'category': category, 'subcategory': subcategory,'flag':flag}
        return render(request, 'shop/addproductdetails.html', params)



    params={'category':category,'subcategory':subcategory,'flag':flag}

    return render(request, 'shop/addproductdetails.html',params)

def allcategory(request):
    category = Category.objects.all()

    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    params = {'category': category,'flag':flag}

    return render(request, 'shop/allcategory.html',params)

def editcategory(request,id):
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    params = {'id':id,'flag':flag}
    if request.method == 'POST':
        category = request.POST['category']

        obj = Category.objects.get(pk=id)
        obj.cat_name= category
        obj.save()
        messages.success(request, "1 category is changed successfully")
        return redirect('allcategory')

    else:
        return render(request, 'shop/editcategory.html',params)

def deletecategory(request,id):

    Category.objects.filter(pk=id).delete()
    messages.success(request, "1 category is deleted successfully")
    return redirect('allcategory')

def allsubcategory(request):
    subcategory = Sub_Category.objects.all()

    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True
    params = {'subcategory': subcategory,'flag':flag}
    return render(request, 'shop/allsubcategory.html',params)

def deletesubcategory(request,id):

    Sub_Category.objects.filter(pk=id).delete()
    messages.success(request, "1 sub category is deleted successfully")
    return redirect('allsubcategory')

def allproductdetails(request):
    product = Product_Details.objects.all()
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    if request.method == 'POST':
        day = request.POST['daytype']
        if day == 'today':
            x = datetime.datetime.now()
            product = Product_Details.objects.filter(prod_date=x)

            return render(request, 'shop/allproductdetails.html', {'product':product,'flag':flag})
        elif day == 'yesterday':
            x= datetime.datetime.now() + timedelta(days=-1)
            product = Product_Details.objects.filter(prod_date=x)

            return render(request, 'shop/allproductdetails.html', {'product': product,'flag':flag})

        elif day == '5daysbefore':
            x= datetime.datetime.now() + timedelta(days=-5)
            product = Product_Details.objects.filter(prod_date=x)

            return render(request, 'shop/allproductdetails.html', {'product': product,'flag':flag})

        elif day == '10daysbefore':
            x= datetime.datetime.now() + timedelta(days=-10)
            product = Product_Details.objects.filter(prod_date=x)

            return render(request, 'shop/allproductdetails.html', {'product': product,'flag':flag})

        elif day == 'allproduct':

            product = Product_Details.objects.all()

            return render(request, 'shop/allproductdetails.html', {'product': product,'flag':flag})


    params={'product':product,'flag':flag}
    return render(request, 'shop/allproductdetails.html',params)

def deleteproductdetails(request,id):

    Product_Details.objects.filter(pk=id).delete()
    messages.success(request, "1 sub product is deleted successfully")
    return redirect('allproductdetails')

def editsubcategory(request,id):
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    if request.method == "POST":
        subcat = request.POST['subcategory']
        upload = request.FILES['img']
        category = request.POST['category']

        cat = Category.objects.filter(cat_id=category).first()

        obj = Sub_Category.objects.get(pk=id)
        obj.sub_cat_name = subcat
        obj.sub_cat_image = upload
        obj.category = cat
        obj.save()
        messages.success(request, "1 sub category is changed successfully")
        return redirect('allsubcategory')

    category = Category.objects.all()
    params = {'category': category,'id':id,'flag':flag}

    return render(request, 'shop/editsubcategory.html', params)

def allmessages(request):
    msgs = Contactus.objects.filter(read = 0)
    params = {'msgs':msgs}
    return render(request,'shop/allmessages.html',params)


def handlemessages(request,id):
    obj = Contactus.objects.get(pk=id)
    obj.read=1
    obj.save()
    return redirect('allmessages')

def ownersearch(request):
    user = None
    flag = False
    if request.user.is_authenticated:
        user = request.user
    if user.is_staff == True and user.is_superuser == False:
        flag = True

    params={'flag':flag}

    return render(request, 'shop/ownersearch.html',params)

def handlecategorysearch(request):

    query = request.GET['categoryquery']
    if len(query) > 78 or len(query) <= 2:
        allPosts = []
    else:
        allPostsname = Category.objects.filter(cat_name__icontains=query)


        allPosts = allPostsname

    params = {'allPosts': allPosts, 'query':query }
    return render(request, 'shop/handlecategorysearch.html', params)

def handlesubcategorysearch(request):
    query = request.GET['subcategoryquery']
    if len(query) > 78 or len(query) <= 2:
        allPosts = []
    else:
        allPostsname = Sub_Category.objects.filter(sub_cat_name__icontains=query)


        allPosts = allPostsname

    params = {'allPosts': allPosts, 'query':query }
    return render(request, 'shop/handlesubcategorysearch.html', params)

def handleproductsearch(request):
    query = request.GET['productquery']
    if len(query) > 78 or len(query) <= 2:
        allPosts = []
    else:
        allPostsname = Product_Details.objects.filter(prod_name__icontains=query)
        allPostsbrand = Product_Details.objects.filter(prod_brand__icontains=query)

        allPosts = allPostsname.union(allPostsbrand)

    params = {'allPosts': allPosts,  'query': query}
    return render(request, 'shop/handleproductsearch.html', params)


def ownerorders(request):
    return render(request,'shop/ownerorders.html')

def notdelivered(request):
    order=Orders.objects.filter(delivered=0)

    count = Orders.objects.filter(delivered=0).count()

    mainlist=[]
    for x in order:
        l=[]

        prod = Order_Details.objects.filter(order_id= x.order_id)

        l.append(x)
        l.append(prod)
        mainlist.append(l)




    #for x in mainlist:
        #print(x[0].first_name)
        #for z in x[1]:
            #print(z.name)
    params={'prods':mainlist,'count':count}



    return render(request,'shop/notdelivered.html',params)


def handleorderpacked(request,id):
    obj = Orders.objects.get(pk=id)
    obj.packed = 1
    obj.save()
    return redirect('notdelivered')

def handleorderondelivery(request,id):
    obj = Orders.objects.get(pk=id)
    obj.ondelivery = 1
    obj.save()
    return redirect('notdelivered')

def handleorderdelivered(request,id):
    obj = Orders.objects.get(pk=id)
    obj.delivered = 1
    x = datetime.datetime.now()
    obj.delivereddate = x

    obj.save()
    return redirect('notdelivered')


def ordercancelled(request):
    order=Orders.objects.filter(canceled=1)

    count = Orders.objects.filter(canceled=1).count()

    mainlist=[]
    for x in order:
        l=[]

        prod = Order_Details.objects.filter(order_id= x.order_id)

        l.append(x)
        l.append(prod)
        mainlist.append(l)




    #for x in mainlist:
        #print(x[0].first_name)
        #for z in x[1]:
            #print(z.name)
    params={'prods':mainlist,'count':count}



    return render(request,'shop/ordercancelled.html',params)


def handleordercancelled(request,id):
    Orders.objects.filter(pk=id).delete()
    messages.success(request, "1 cancelled order is deleted successfully")
    return redirect('ordercancelled')

def orderreturned(request):
    order = Orders.objects.filter(order_return=1)

    count = Orders.objects.filter(order_return=1).count()

    mainlist = []
    for x in order:
        l = []

        prod = Order_Details.objects.filter(order_id=x.order_id)
        msg = Return_Message.objects.filter(order_id=x.order_id)

        l.append(x)
        l.append(prod)
        l.append(msg)
        mainlist.append(l)

    # for x in mainlist:
    # print(x[0].first_name)
    # for z in x[1]:
    # print(z.name)
    params = {'prods': mainlist, 'count': count}

    return render(request, 'shop/orderreturned.html', params)


def handleorderreturned(request,id):
    Orders.objects.filter(pk=id).delete()
    messages.success(request, "1 returned order is deleted successfully")
    return redirect('orderreturned')


def orderdelivered(request):
    order = Orders.objects.filter(delivered=1)

    count = Orders.objects.filter(delivered=1).count()

    mainlist = []
    for x in order:
        l = []

        prod = Order_Details.objects.filter(order_id=x.order_id)


        l.append(x)
        l.append(prod)

        mainlist.append(l)

    # for x in mainlist:
    # print(x[0].first_name)
    # for z in x[1]:
    # print(z.name)
    params = {'prods': mainlist, 'count': count}

    return render(request, 'shop/orderdelivered.html', params)

def addemployee(request):
    return render(request, 'shop/addemployee.html')

def handleowneraddemployee(request):
    if request.method == 'POST':

        usersname = request.POST['usersname']
        userfirstname = request.POST['userfirstname']
        userlastname = request.POST['userlastname']
        useremail = request.POST['useremail']
        usermobileno = request.POST['usermobileno']
        userpassword = request.POST['userpassword']
        userconfirmpassword = request.POST['userconfirmpassword']

        if len(usersname) < 5:
            messages.error(request,
                           "User name must be greater than 4 character and contains alphabet,number and special character ")
            return redirect('addemployee')
        if User.objects.filter(username=usersname).exists():
            messages.error(request, "this username has already taken try other one")
            return redirect('addemployee')

        if len(userfirstname) < 3:
            messages.error(request, "name must be greater than 2 character")
            return redirect('addemployee')

        if not userfirstname.isalpha():
            messages.error(request, "name must contain alphabets only")
            return redirect('addemployee')

        if User.objects.filter(email=useremail).exists():
            messages.error(request, "this email  already exists")
            return redirect('addemployee')

        def isValid(s):
            Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
            return Pattern.match(s)

        if (not isValid(usermobileno)):
            messages.error(request, "invalid mobile number")
            return redirect('addemployee')

        if userpassword != userconfirmpassword:
            messages.error(request, "password and confirm password must be same")
            return redirect('addemployee')

        myuser = User.objects.create_user(usersname, useremail, userpassword)

        myuser.first_name = userfirstname
        myuser.last_name = userlastname

        myuser.is_staff=True
        myuser.is_superuser = False

        myuser.save()
        mobile = Mobileno(mobileno= usermobileno, user=myuser)
        mobile.save()

        messages.success(request, "1 Employee added successfully")

        return redirect('addemployee')




    else:
        return redirect('addemployee')



def allemployee(request):
    user = User.objects.filter(is_staff= True).filter(is_superuser=False)
    mainlist=[]




    for x in user:
        l=[]

        mobile = Mobileno.objects.filter(user_id = 11).first()

        l.append(x)
        l.append(mobile)
        mainlist.append(l)

    params={'list':mainlist}

    return render(request, 'shop/allemployee.html',params)

def allusers(request):
    user = User.objects.filter(is_staff=False).filter(is_superuser=False)

    print(user)
    params = {'prods': user}

    return render(request, 'shop/allusers.html', params)

def handleemployeedelete(request,id):
    User.objects.filter(pk=id).delete()
    messages.success(request, "1 employee deleted successfully")
    return redirect('allemployee')

def editproductdetails(request,id):


    category = Category.objects.all()
    subcategory = Sub_Category.objects.all()
    if request.method == 'POST':
        prodname = request.POST['prodname']
        prodbrand = request.POST['prodbrand']
        prodpacketsize = request.POST['prodpacketsize']
        prodpackettype = request.POST['prodpackettype']
        prodmrp = request.POST['prodmrp']
        prodprice = request.POST['prodprice']
        upload = request.FILES['img']
        catid = request.POST['category']
        subcatid = request.POST['subcategory']
        cat = Category.objects.filter(cat_id=catid).first()
        subcat = Sub_Category.objects.filter(sub_cat_id=subcatid).first()

        obj = Product_Details.objects.get(pk=id)

        obj.prod_name = prodname
        obj.prod_brand = prodbrand
        obj.prod_packet_size=prodpacketsize
        obj.prod_packet_size = prodpackettype

        obj.prod_mrp=prodmrp
        obj.prod_price=prodprice
        obj.prod_image=upload

        obj.category = cat
        obj.subcategory=subcat
        obj.save()

        messages.success(request, "1 product is changed successfully")

        params = {'category': category, 'subcategory': subcategory,'id':id}
        return redirect('allproductdetails')

    params = {'category': category, 'subcategory': subcategory, 'id':id}

    return render(request, 'shop/editproductdetails.html', params)


def ownerlogin(request):
    return render(request, 'shop/ownerlogin.html')

def handleownerlogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None and (user.is_staff==True or user.is_superuser==True):
            login(request,user)
            messages.success(request, "User Successfully Logged in")
            return redirect('ownerhome')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('ownerlogin')
    else:
        return redirect('ownerlogin')


def handleownerlogout(request):
    logout(request)
    messages.success(request, "successfully Logged Out")
    return redirect('ownerlogin')

def addcoupon(request):

    if request.method=='POST':
        couponname=request.POST['coupon']
        coupon=Coupon(coupon_name=couponname)
        coupon.save()
        messages.success(request,'Coupon is added successfully')
    coupons = Coupon.objects.all()
    params = {'coupons': coupons}
    return render(request, 'shop/addcoupon.html',params)

def deletecoupon(request,id):
    Coupon.objects.filter(pk=id).delete()
    messages.success(request, "1 coupon deleted successfully")
    return redirect('addcoupon')









