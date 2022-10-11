from django.contrib import admin
from .models import *


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['pk', 'pname', 'pprice','pquantity']
    search_fields = ('pname','pprice')
    list_editable = ['pprice','pquantity']
    list_display_links = ['pname']


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['pk', 'Catitle', 'CaSubTitle','Status']
    search_fields = ('Catitle',)
    list_editable = ['Status']
    list_display_links = ['Catitle']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'plant', 'customer','status','quantity','price','address','bkashTrxID','date']
    search_fields = ('plant__pname','customer__username','bkashTrxID','price')
    list_editable = ['status']
    list_display_links = ['plant']

@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ['pk',  'email', 'fname','message']
    search_fields = ('email','fname','lname', 'message')
    list_display_links = ['email']

