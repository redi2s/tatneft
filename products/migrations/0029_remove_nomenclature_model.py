# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-19 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_auto_20161219_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomenclature',
            name='model',
        ),
    ]
