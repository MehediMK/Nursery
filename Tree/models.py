from django.db import models
from django.contrib.auth.models import User
import datetime

class Plant(models.Model):
    pname = models.CharField(max_length=150,verbose_name="Plants Name")
    pimage = models.ImageField(upload_to='plantimage',blank=False,verbose_name='Plant Image')
    ptype = models.CharField(max_length=100,blank=True,verbose_name='Season Type')
    plight = models.CharField(max_length=100,blank=True,verbose_name='Growth Area')
    pprice = models.IntegerField(verbose_name='Plant Price')
    pmaintain = models.CharField(max_length=100,blank=True,verbose_name='Maintainance')
    pwatersc = models.CharField(max_length=100,blank=True,verbose_name='Water Schedule')
    pdesc = models.TextField(max_length=600,blank=True,verbose_name='Description')
    pquantity = models.IntegerField(verbose_name='Quantity')

    def __str__(self):
        return self.pname
    
    @staticmethod
    def get_product_by_id(ids):
        return Plant.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Plant.objects.all()
    
    def short_desc(self):
        return self.pdesc[:50]

# carousel model here
class Carousel(models.Model):
    Catitle = models.CharField(max_length=100,verbose_name='Title',blank=False)
    CaSubTitle = models.CharField(max_length=150,verbose_name='Subtitle',blank=False)
    CaImage = models.ImageField(upload_to='carouselImage',verbose_name='Image',blank=False)
    CaDesc = models.TextField(max_length=300,verbose_name='Description',blank=False)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Catitle

    def desc(self):
        return self.CaDesc[:100]


class Order(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    bkashTrxID = models.CharField(max_length=150,default='',blank=True)
    address = models.CharField(max_length=150,default='')
    phone = models.CharField(max_length=15,default='')
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.address
    


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-id')


class Contactus(models.Model):
    fname=models.CharField(max_length=20,blank=False)
    lname=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=40,blank=False)
    message = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.email

