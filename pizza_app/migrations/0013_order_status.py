# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0012_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order_received', 'order_received'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered'), ('not delivered', 'not delivered')], default=1, max_length=23),
        ),
    ]
