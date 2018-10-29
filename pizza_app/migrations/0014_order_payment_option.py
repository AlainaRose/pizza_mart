# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0013_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('cas_on_delivery', 'cash_on_delivery'), ('online_pay', 'online_pay')], default=1, max_length=20),
        ),
    ]