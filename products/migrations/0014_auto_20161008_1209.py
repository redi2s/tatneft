# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20161007_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='weight_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bid',
            name='weight_unit',
            field=models.FloatField(default=0),
        ),
    ]