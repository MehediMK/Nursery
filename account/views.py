import re
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from .forms import UserSignUpForm,UserInfo

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('successfully login in')
                return redirect('home')
            else:
                return render(request,'account/login.html')
        else:
            return render(request,'account/login.html')
    else:
        return redirect('home')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')

def signup_view(request):
    form = UserSignUpForm()
    form1 = UserInfo()
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        form1 = UserInfo(request.POST , request.FILES or None)        

        if form.is_valid() and form1.is_valid():
            print(form1.cleaned_data['profile_pic'])
            userform = form.save()
            userinfo = form1.save(commit=False)
            userinfo.user = userform
            userinfo.save()
            return redirect('login')    

    return render(request,'account/signup.html',context={'form':form,'form1':form1})

