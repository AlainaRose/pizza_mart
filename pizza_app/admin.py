# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin



from pizza_app.models import Customer
from pizza_app.models import Menu
from pizza_app.models import order

admin.site.register(Menu)


admin.site.register(Customer)

admin.site.register(order)
