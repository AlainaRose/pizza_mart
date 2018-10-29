from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	address=models.CharField(max_length=10)
	phone=models.IntegerField()
	created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return (self.name)


class Menu(models.Model):
	item_name=models.CharField(max_length=20)
        price = models.DecimalField(max_digits=10, decimal_places=2)
	created_date=models.DateTimeField(auto_now=True)
        item_photo=models.ImageField(upload_to='media')
        def __str__(self):
		return (self.item_name)


      
class order(models.Model):
   
        username=models.OneToOneField(Customer,on_delete=models.CASCADE,default=True)
        address=models.TextField(max_length=40)
        items=models.OneToOneField(Menu,on_delete=models.CASCADE,default=True)
 
	created_date=models.DateTimeField(auto_now=True)
        quantity=models.IntegerField(default=1)
	def __str__(self):
		return (self.name)

