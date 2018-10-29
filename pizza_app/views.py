from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,FormView,View
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from pizza_app.forms import UserForm,RegisterForm,MenuCreateForm,orderform
from pizza_app.models import Customer
from pizza_app.models import Menu
from pizza_app.models import order
from django.views.generic.edit import DeleteView
import json
import urllib
from django.conf import settings
from django.contrib import messages
from pizza_app.models import Customer
from pizza_app.forms import RegisterForm,orderform,MenuCreateForm


import logging, traceback

from django.views.decorators.csrf import csrf_exempt
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
import logging, traceback
import pizza_app.constants as constants
import pizza_app.config as config
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt

def payment(request):   
    data = {}
    txnid = get_transaction_id()
    hash_ = generate_hash(request, txnid)
    hash_string = get_hash_string(request, txnid)
    # use constants file to store constant values.
    # use test URL for testing
    data["action"] = constants.PAYMENT_URL_LIVE 
    data["amount"] = float(constants.PAID_FEE_AMOUNT)
    data["productinfo"]  = constants.PAID_FEE_PRODUCT_INFO
    data["key"] = config.KEY
    data["txnid"] = txnid
    data["hash"] = hash_
    data["hash_string"] = hash_string
  
    data["service_provider"] = constants.SERVICE_PROVIDER
    data["furl"] = request.build_absolute_uri(reverse("payment_failure"))
    data["surl"] = request.build_absolute_uri(reverse("payment_success"))
    
    return render(request, "payment.html", data)        
    
# generate the hash
def generate_hash(request, txnid):
    try:
        # get keys and SALT from dashboard once account is created.
        # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string = get_hash_string(request,txnid)
        generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        # log the error here.
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

# create hash string using all the fields
def get_hash_string(request, txnid):
    hash_string = config.KEY+"|"+txnid+"|"+str(float(constants.PAID_FEE_AMOUNT))+"|"+constants.PAID_FEE_PRODUCT_INFO+"|"
    
    hash_string += "||||||||||"+config.SALT

    return hash_string

# generate a random transaction Id.
def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
    # take approprite length
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid

# no csrf token require to go to Success page. 
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
    data = {}
    return render(request, "payment/success.html", data)

# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    return render(request, "payment/failure.html", data)


class AdminPage(TemplateView):
    template_name='adminhome.html'
#*******************************admin****************************************8


@login_required
def home(request):
    return render(request, 'core/home.html')

class successview(View):
	template_name='success.html'
class failureview(View):
	template_name='failure.html'
     

class HomeView(TemplateView):
	template_name='home.html'

class View(View):
	"""docstring for FirstView"""
	template_name="userhome.html"

	def get(self,request):
		return render(request,self.template_name)
	

class ContactView(TemplateView):
	template_name='Contact.html'



class MenuView(TemplateView):
	template_name='menu.html'

class MenuCreateView(CreateView):
        template_name='createmenu.html'
        form_class=MenuCreateForm
        success_url='success'


class MenuView(TemplateView):
	template_name='menu.html'

	success_url='success'

class ListMenu(ListView):
	template_name="menulist.html"
	model=Menu


class UpdateMenu(UpdateView):
	model=Menu
	template_name="updatemenu.html"
	success_url='/listmenu/'
	form_class=MenuCreateForm



class ListUser(ListView):
	template_name="listuser.html"
	model=User
        context_object='list'

class ordernow(CreateView):
        template_name='ordernow.html'
        success_url='/payment/'
        form_class=orderform
      
        

class ordersuccess(TemplateView):
	template_name='ordersuccess.html'



def login(request):
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/adminhome/")# or your url name
         if request.user.is_staff:
             return redirect("/userhome/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/adminpage/")# or your url name
             if request.user.is_staff:
                 return redirect("/userhome/")# or your url name

         else:
             messages.error(request, 'Error wrong username/password')
     context = {}
     context['form']=form

     return render(request, 'login.html', context)

@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
     context = {}
     return render(request, 'userhome.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
     context = {}
     return render(request, 'adminpage.html', context)
    

	
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserForm
    model = Customer
    

    def get(self, request, *args, **kwargs):
        self.object=None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        register_form = RegisterForm()
        return self.render_to_response(self.get_context_data(form1=user_form,form2=register_form))
    

    def post(self, request, *args, **kwargs):
        self.object=None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        register_form = RegisterForm(self.request.POST,self.request.FILES)

        if (user_form.is_valid() and register_form.is_valid()):
            return self.form_valid(user_form,register_form)
        else: 
            return self.form_invalid(user_form,register_form)

    def form_valid(self,user_form,register_form):

        self.object = user_form.save()
        self.object.is_staff=True
        self.object.save()
        p = register_form.save(commit=False)
        p.user = self.object
        p.save()
        return redirect('/login/')


    def form_invalid(self,user_form,register_form):
        return self.render_to_response(self.get_context_data(form1=user_form,form2=register_form)) 



