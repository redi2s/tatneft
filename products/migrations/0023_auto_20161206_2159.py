# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_bidcomposition_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidcomposition',
            name='amount',
            field=models.FloatField(),
        ),
    ]