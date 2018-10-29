from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from pizza_app.models import Customer

from pizza_app.models import Menu


from pizza_app.models import order



                
class MenuCreateForm(forms.ModelForm):
	class Meta:
            model = Menu 
            exclude=('create_date',)





class UserForm(UserCreationForm):
	class Meta:
		model=User
                fields=['username','email']

class RegisterForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=['address','phone']
                success_url='success'


class orderform(forms.ModelForm):
	class Meta():
		model=order
		exclude=("create_date",)








