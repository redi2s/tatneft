# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-19 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20161219_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Материал'},
        ),
    ]
