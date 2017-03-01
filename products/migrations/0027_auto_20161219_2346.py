# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-19 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20161211_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='Количество')),
            ],
            options={
                'verbose_name_plural': 'Материалы',
                'verbose_name': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Номенклатура')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Model')),
            ],
            options={
                'verbose_name_plural': 'Номенклатура',
                'verbose_name': 'Номенклатура',
            },
        ),
        migrations.AddField(
            model_name='materials',
            name='nomenclature1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomenclature1', to='products.Nomenclature'),
        ),
        migrations.AddField(
            model_name='materials',
            name='nomenclature2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomenclature2', to='products.Nomenclature'),
        ),
    ]