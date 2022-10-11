from django.urls import path
from .views import user_login,user_logout,signup_view

urlpatterns = [
    path('',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('signup/',signup_view,name='signup'),
    
]