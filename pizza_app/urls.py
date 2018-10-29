from django.conf.urls import url,include
from django.contrib import admin
from pizza_app.views import HomeView,RegisterView,AdminPage,View,ContactView,MenuView,ListUser,MenuCreateView,MenuView,ListMenu,UpdateMenu,ordernow,payment,ordersuccess,failureview,successview
from pizza_app import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth import views as auth_views
from pizza_app import views



urlpatterns = [
    url(r'^home/',HomeView.as_view(),name='home'),
    url(r'^userhome',View.as_view(),name='userhome'),
    url(r'^about/',HomeView.as_view(),name='about'),
    url(r'^Contact',ContactView.as_view(),name='Contact'),
    url(r'^menu/',MenuView.as_view(),name='menu'),
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^login/',views.login, name='login'),
    url(r'^ordernow/',ordernow.as_view(),name='ordernow'),

   


    url(r'^adminpage/',AdminPage.as_view(),name='adminpage'),
    url(r'^listuser/',ListUser.as_view(),name='listuser'),
    url(r'^menu/',MenuView.as_view(),name='menu'),
    url(r'^createmenu/',MenuCreateView.as_view(),name='createmenu'),  
    url(r'^listmenu/',ListMenu.as_view(),name='listmenu'),
    url(r'^update/(?P<pk>[0-9]+)/$',UpdateMenu.as_view(),name='update'),

   

  
    url(r'^payment/$', views.payment, name="payment"),
    url(r'^payment/success$', views.payment_success, name="payment_success"),
    url(r'^payment/failure$', views.payment_failure, name="payment_failure"),



    

]
  
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

