# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20161027_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidcomposition',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
