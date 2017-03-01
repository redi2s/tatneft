# -*- coding: utf-8 -*-

from django.forms import ModelForm, SelectDateWidget
from django import forms
from django.contrib.admin import widgets
from products.models import Bid, Composition, Rawmaterial

class DateInput(forms.DateInput):
    input_type = 'date'

class BidForm(ModelForm):
    # dt = forms.DateField(widget=SelectDateWidget)
    # dt1 = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    # dt2 = forms.DateField(widget=DateInput)

    class Meta:
        model = Bid
        fields = ['date', 'product', 'model', 'size', 'amount_psc', 'weight_unit', 'material', 'delivery_date', 'color', 'customer']
        # widgets = {
        #     'date': forms.DateInput(attrs={'class': 'datepicker'}),
        #     'delivery_date': forms.DateInput(attrs={'class': 'datepicker'}),
        # }

    def __init__(self, *args, **kwargs):
        super(BidForm, self).__init__(*args, **kwargs)
        # for field in self.fields:
            # self.fields[field].widget.attrs['class'] = 'form-control'
            # self.fields[field].label_classes = ('col-sm-2 control-label',)
        self.fields['date'].widget.attrs['class'] = 'form-control datepicker'
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['product'].empty_label = 'Выберите значение'
        self.fields['model'].widget.attrs['class'] = 'form-control'
        # self.fields['model'].initial = '5'
        self.fields['size'].widget.attrs['class'] = 'form-control'
        self.fields['amount_psc'].widget.attrs['class'] = 'form-control'
        self.fields['weight_unit'].widget.attrs['class'] = 'form-control'
        self.fields['material'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_date'].widget.attrs['class'] = 'form-control datepicker'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['customer'].widget.attrs['class'] = 'form-control'

        # self.fields['date'].widget = widgets.AdminDateWidget()
        # self.fields['date'].widget = widgets.AdminDateWidget()
        # self.fields['year'].widget = widgets.AdminDateWidget()
        # self.fields['color'].widget = widgets.AdminSplitDateTime()
        # self.fields['delivery_date'].widget = widgets.AdminDateWidget()

    def save(self, commit=True):
        obj = super(BidForm, self).save(commit=False)
        obj.date = self.cleaned_data['date']
        obj.product = self.cleaned_data['product']
        obj.model = self.cleaned_data['model']
        size = self.cleaned_data['size']
        obj.size = size
        obj.amount_psc = self.cleaned_data['amount_psc']
        amount_meter = (float(size.name) * float(self.cleaned_data['amount_psc'])) / 1000
        obj.amount_meter = amount_meter
        weight_unit = float(self.cleaned_data['weight_unit'])
        obj.weight_unit = weight_unit
        obj.weight_total = weight_unit * amount_meter
        obj.material = self.cleaned_data['material']
        obj.color = self.cleaned_data['color']
        obj.customer = self.cleaned_data['customer']
        if commit:
            obj.save()
            # print('obj =', obj.id, 'type =', type(obj))
        return obj

class CompositionForm(ModelForm):
    class Meta:
        model = Composition
        fields = ['name', 'model', 'unit', 'expense', 'loss', 'ismanufacture']

    def __init__(self, *args, **kwargs):
        super(CompositionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['model'].widget.attrs['class'] = 'form-control'
        self.fields['unit'].widget.attrs['class'] = 'form-control'
        self.fields['expense'].widget.attrs['class'] = 'form-control'
        self.fields['loss'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        obj = super(CompositionForm, self).save(commit=False)
        obj.name = self.cleaned_data['name']
        obj.model = self.cleaned_data['model']
        obj.unit = self.cleaned_data['unit']
        expense = float(self.cleaned_data['expense'])
        obj.expense = expense
        loss = float(self.cleaned_data['loss'])
        obj.loss = loss
        obj.total_expense = expense + loss
        if commit:
            obj.save()
        return obj

class RawmaterialForm(ModelForm):
    class Meta:
        model = Rawmaterial
        exclude = ('series',)

    def __init__(self, *args, **kwargs):
        super(RawmaterialForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        obj = super(RawmaterialForm, self).save(commit=False)
        obj.composition = self.cleaned_data['composition']
        obj.name = self.cleaned_data['name']
        obj.ral = self.cleaned_data['ral']
        obj.rm_profile = self.cleaned_data['rm_profile']
        rm_profile = float(self.cleaned_data['rm_profile'])
        obj.rm_repurposing = self.cleaned_data['rm_repurposing']
        obj.series = rm_profile * 1000
        if commit:
            obj.save()
        return obj

