from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.index2, name='shophome'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path("productview/<int:id>", views.productview, name='productview'),
    #path("productview2/<int:id>", views.productview2, name='productview2'),

    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    path('tracker/', views.tracker, name='tracker'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('shophome/', views.shophome, name='shophome'),
    path('bottomsearch/', views.bottomsearch, name='bottomsearch'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('payment/', views.payment, name='payment'),
    path('userorder/', views.userorder, name='userorder'),
    path('handleuserorder/', views.handleuserorder, name='handleuserorder'),
    path('handleuserordercancelled/<int:id>', views.handleuserordercancelled, name='handleuserordercancelled'),
    path('handleuserorderreturned/<int:id>', views.handleuserorderreturned, name='handleuserorderreturned'),
    path('useraccount/', views.useraccount, name='useraccount'),

    path('ownerhome/', views.ownerhome, name='ownerhome'),
    path('addcategory/', views.addcategory, name='addcaegory'),
    path('addsubcategory/', views.addsubcategory, name='addsubcaegory'),
    path('addproductdetails/', views.addproductdetails, name='addproductdetails'),

    path('allcategory/', views.allcategory, name='allcategory'),
    path("editcategory/<int:id>", views.editcategory, name='editcategory'),
    path('deletecategory/<int:id>', views.deletecategory, name='deletecategory'),

    path('allsubcategory/', views.allsubcategory, name='allsubcategory'),
    path('deletesubcategory/<int:id>', views.deletesubcategory, name='deletesubcategory'),
    path('editsubcategory/<int:id>', views.editsubcategory, name='editsubcategory'),

    path('allproductdetails/', views.allproductdetails, name='allproductdetails'),
    path('deleteproductdetails/<int:id>', views.deleteproductdetails, name='deleteproductdetails'),

    path('allmessages/', views.allmessages, name='allmessages'),
    path('handlemessages/<int:id>', views.handlemessages, name='handlemessages'),

    path('ownersearch/', views.ownersearch, name='ownersearch'),
    path('handlecategorysearch/', views.handlecategorysearch, name='handlecategorysearch'),
    path('handlesubcategorysearch/', views.handlesubcategorysearch, name='handlesubcategorysearch'),
    path('handleproductsearch/', views.handleproductsearch, name='handleproductsearch'),

    path('ownerorders/', views.ownerorders, name='ownerorders'),
    path('notdelivered/', views.notdelivered, name='notdelivered'),

    path('handleorderpacked/<int:id>', views.handleorderpacked, name='handleorderpacked'),
    path('handleorderondelivery/<int:id>', views.handleorderondelivery, name='handleorderondelivery'),
    path('handleorderdelivered/<int:id>', views.handleorderdelivered, name='handleorderdelivered'),

    path('ordercancelled/', views.ordercancelled, name='ordercancelled'),

    path('handleordercancelled/<int:id>', views.handleordercancelled, name='handleordercancelled'),

    path('orderreturned/', views.orderreturned, name='orderreturned'),
    path('handleorderreturned/<int:id>', views.handleorderreturned, name='handleorderreturned'),

    path('orderdelivered/', views.orderdelivered, name='orderdelivered'),

    path('addemployee/', views.addemployee, name='addemployee'),
    path('handleowneraddemployee/', views.handleowneraddemployee, name='handleowneraddemployee'),

    path('allemployee/', views.allemployee, name='allemployee'),
    path('allusers/', views.allusers, name='allusers'),

    path('handleemployeedelete/<int:id>', views.handleemployeedelete, name='handleemployeedelete'),
    path('editproductdetails/<int:id>', views.editproductdetails, name='editproductdetails'),

    path('ownerlogin/', views.ownerlogin, name='ownerlogin'),
    path('handleownerlogin/', views.handleownerlogin, name='handleownerlogin'),
    path('handleownerlogout/', views.handleownerlogout, name='handleownerlogout'),

    path('addcoupon/', views.addcoupon, name='addcoupon'),
    path('deletecoupon/<int:id>', views.deletecoupon, name='deletecoupon'),

]
