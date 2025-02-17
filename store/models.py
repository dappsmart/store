from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(default=00000, max_length=200, blank=False)
    #price = models.DecimalField(default=0, on_delete=SET_NULL, max_digits=10, decimal_places=2, blank=False, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(default=False, blank=True)
    
    def __str__(self):
         return self.name #+ : $" + str(self.price)
    
    @property
    def imageURL(self):
        try: 
            url = self.image.url 
        except:
            url = ''    
        return url    
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=SET_NULL, null=True, blank=True )      
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(primary_key=True, editable=False, max_length=200, blank=True)
    
    def __str__(self):
        return str(self.id) 
 
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total      
    
    
# class OrderItem(models.Model):   
#     product = models.ForeignKey(Product, on_delete=SET_NULL, null=True, blank=False)
#     order = models.ForeignKey(Order, on_delete=SET_NULL, null=True, blank=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
    
#     def get_total(self):
#         total = str(self.product.price * self.quantity)        
#         return total
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True) 
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    
    