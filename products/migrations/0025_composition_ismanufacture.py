# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_rawmaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='ismanufacture',
            field=models.BooleanField(default=0, verbose_name='Собственное производство'),
        ),
    ]