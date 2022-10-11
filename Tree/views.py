from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from account.forms import UserSignUpForm,UserInfo,UserFLEname
from account.models import User_info
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    plants = Plant.get_all_products()

    # carousel here
    carousels = Carousel.objects.filter(Status=True).order_by('-pk')[:3]

    context={
        'plants':plants,
        'carousels':carousels,
    }
    return render(request,"product/index.html",context)


def add_to_cart(request):
    if request.method == "POST":
        product = request.POST.get('plant')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            item = cart.get(product)
            if item:
                if remove:
                    if item<=1:
                        cart.pop(product)
                    else:
                        cart[product] = item-1
                else:
                    cart[product] = item+1
            else:
                cart[product] = 1
        
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
    return redirect('home')


def cart(request):
    mycart = request.session.get('cart')
    if mycart:
        ids = list(request.session.get('cart').keys())
        plant = Plant.get_product_by_id(ids)
        print(plant)
        return render(request,'product/cart.html',{'plants':plant})
    else:
        request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        plant = Plant.get_product_by_id(ids)
        print(plant)
        return render(request,'product/cart.html',{'plants':plant})


def incdec(request):
        product = request.POST.get('productid')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('cart')


def checkout(request):
    address = request.POST.get('address')
    bkashtrxid = request.POST.get('bkashtrxid')
    phone = request.POST.get('phone')
    customer = request.user
    cart = request.session.get('cart')
    plants = Plant.get_product_by_id(list(cart.keys()))
    print(address, phone, customer, cart, plants,bkashtrxid)

    for plant in plants:
        # print(cart.get(str(product.id)))
        order = Order(customer=customer,
                        plant=plant,
                        price=plant.pprice,
                        bkashTrxID=bkashtrxid,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(plant.id)))
        order.save()
        print(customer,plant,plant.pprice,address,phone,cart.get(str(plant.id)),bkashtrxid)
    request.session['cart'] = {}

    return redirect('cart')



@login_required(redirect_field_name='login')
def orderView(request):
    customer = request.user
    orders = Order.get_orders_by_customer(customer) 
    print(orders)
    return render(request,'product/order.html',{'orders':orders})




@login_required(redirect_field_name='login')
def user_profile(request):
    user = request.user    
    # get user
    user_profile = User_info.objects.get(user=user)
    orders = Order.get_orders_by_customer(user) 
    context = {
        'user':user,
        'profile':user_profile,
        'orders':orders,
    }
    return render(request,'product/dashboard.html',context)

@login_required(redirect_field_name='login')
def editUserInfo(request):
    if request.method == 'POST':
        mydata = User_info.objects.get(user=request.user)
        user = User.objects.get(username=request.user.username)
        form = UserInfo( request.POST, request.FILES or None, instance=mydata)
        form1 = UserFLEname( request.POST, request.FILES or None, instance=user)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
        return redirect('userprofile')
    else:
        mydata = User_info.objects.get(user=request.user)
        user = User.objects.get(username=request.user.username)
        form = UserInfo(instance=mydata)
        form1 = UserFLEname(instance=user)
    context={
        'form':form,
        'form1':form1,
        'userinfo':mydata,
    }
    return render(request,'product/editinfo.html',context)

def productSearch(request):  
    context = {}  
    mysearch = request.GET.get('search')
    print(mysearch)
    context['mysearch'] = mysearch

    products = None

    message = None
    # here get product by search name
    if mysearch:
        myproductsearch = Plant.objects.filter(pname__icontains=mysearch)
        if myproductsearch:
            products=myproductsearch
        else:
            message = 'Search not found'
    else:
        products = Plant.objects.all()
    # here check plant or not th
    if message:
        context['message'] = message
    else:        
        # this query for pagination
        productview = request.GET.get('productview', 1)
        home_paginator = Paginator(products, 12)
        try:
            products_list = home_paginator.page(productview)
            context['plants'] = products_list
        except PageNotAnInteger:
            products_list = home_paginator.page(1)
            context['plants'] = products_list
        except EmptyPage:
            products_list = home_paginator.page(home_paginator.num_pages)
            context['plants'] = products_list
        # end pagination query

    return render(request,'product/search.html',context)




def contactus(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contactus(fname = fname,lname=lname,email=email,message=message)
        contact.save()
        return redirect('home')
    return render(request,'basic/contact.html')

def aboutus(request):
    
    return render(request,'basic/aboutus.html')