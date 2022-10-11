from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="home"),
    path('productSearch/',productSearch,name="productSearch"),
    path('add-to-card/',add_to_cart,name="addtocard"),
    path('cart/',cart,name='cart'),
    path('incdec/',incdec,name='incdec'),
    path('checkout/',checkout,name='checkout'),
    path('orderView/',orderView,name='orderView'),
    path('userprofile/',user_profile,name='userprofile'),
    path('editUserInfo/',editUserInfo,name='editUserInfo'),

    # basic url
    path('contactus/',contactus,name='contactus'),
    path('aboutus/',aboutus,name='aboutus'),

    
]
