# -*- coding: utf-8 -*-

from django.contrib import admin
from products.models import Product, Model, Composition, Size, Material, Customer, Bid, Rawmaterial, Materials, Nomenclature

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')

class CompositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'unit', 'ismanufacture')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BidAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'model', 'size', 'material', 'delivery_date', 'color', 'customer')

class RawmaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('nomenclature1', 'nomenclature2', 'count')

admin.site.register(Product, ProductAdmin)
admin.site.register(Composition, CompositionAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Rawmaterial, RawmaterialAdmin)
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Materials, MaterialsAdmin)
