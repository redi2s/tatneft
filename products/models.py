# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import now

class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Продукты'
        verbose_name = u'Продукт'

class Model(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Модели'
        verbose_name = u'Модель'

class Composition(models.Model):
    name = models.CharField(max_length=255, default=0, verbose_name=u'Наименование материалов')
    model = models.ForeignKey(Model, default=1, verbose_name=u'Модель')
    unit = models.CharField(max_length=255, default=0, verbose_name=u'Ед. измерения')
    expense = models.FloatField(default=0, verbose_name=u'Норма расхода')
    loss = models.FloatField(default=0, verbose_name=u'Потери')
    total_expense = models.FloatField(default=0, verbose_name=u'Итого норма расхода')
    ismanufacture = models.BooleanField(default=0, verbose_name='Собственное производство')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Состав'
        verbose_name = u'Состав'

class Size(models.Model):
    name = models.CharField(max_length=255, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Размеры'
        verbose_name = u'Размер'

class Material(models.Model):
    name = models.CharField(max_length=255, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Материал'
        verbose_name = u'Материал'

class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Контрагенты'
        verbose_name = u'Контрагент'

class Bid(models.Model):
    date = models.DateField(default=now)
    # year = models.DateField(default=now)
    product = models.ForeignKey(Product)
    model = models.ForeignKey(Model)
    size = models.ForeignKey(Size)
    amount_psc = models.IntegerField(default=0)
    amount_meter = models.FloatField(default=0)
    weight_unit = models.FloatField(default=0)
    weight_total = models.FloatField(default=0)
    material = models.ForeignKey(Material)
    delivery_date = models.DateField(default=now)
    color = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural = u'Заявки'
        verbose_name = u'Заявка'

class Temp(models.Model):
    month = models.DateField()
    model = models.ForeignKey(Model)
    amount = models.IntegerField(default=0)

class BidComposition(models.Model):
    bid = models.ForeignKey(Bid)
    product = models.ForeignKey(Product)
    model = models.ForeignKey(Model)
    composition = models.ForeignKey(Composition)
    amount = models.FloatField()

class Rawmaterial(models.Model):
    composition = models.ForeignKey(Composition, verbose_name=u'Комплектующая')
    name = models.CharField(max_length=255, verbose_name=u'Наименование сырья')
    ral = models.CharField(max_length=255, verbose_name=u'RAL')
    rm_profile = models.FloatField(verbose_name=u'Сырьё на профиль, кг/м')
    rm_repurposing = models.FloatField(verbose_name=u'Сырьё на переналадку, кг')
    series = models.FloatField(verbose_name=u'Серия, кг/1000 м.п.')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = u'Сырьё'
        verbose_name = u'Сырьё'

class Nomenclature(models.Model):
    # model = models.ForeignKey(Model)
    name = models.CharField(max_length=255, verbose_name=u'Номенклатура')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = u'Номенклатура'
        verbose_name = u'Номенклатура'

class Materials(models.Model):
    nomenclature1 = models.ForeignKey(Nomenclature, related_name='nomenclature1')
    nomenclature2 = models.ForeignKey(Nomenclature, related_name='nomenclature2')
    count = models.FloatField(verbose_name=u'Количество')

    class Meta:
        verbose_name_plural = u'Материалы'
        verbose_name = u'Материалы'
