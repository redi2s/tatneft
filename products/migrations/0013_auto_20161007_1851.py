# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20161007_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Model', verbose_name='Модель'),
        ),
    ]
