# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20161008_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('amount', models.IntegerField(default=0)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Model')),
            ],
        ),
    ]