# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf

from products.forms import BidForm, CompositionForm, RawmaterialForm
from products.models import Bid, Composition, Temp, Model, BidComposition, Rawmaterial

from django.db.models import Sum, Count, Case, When, IntegerField, CharField, Max, Min
from django.db.models.functions import TruncDay, TruncMonth, TruncYear, ExtractMonth, Extract

import datetime, decimal

from django.utils.timezone import now

@login_required
def bid(request):
    args = {}
    args.update(csrf(request))
    args['bids'] = Bid.objects.all()
    # args['q'] = Bid.objects.values('product__name').annotate(Count('product'))
    args['q'] = Bid.objects.values('product__name').\
        annotate(Sum('size__name'), Sum('amount_psc'), Sum('amount_meter'), Sum('weight_unit'), Sum('weight_total'))
    # args['q'] = Bid.objects.values()
    # args['z'] = Bid.objects.annotate(month=TruncMonth('delivery_date')).values('month').annotate(Sum('amount_psc'))
    # args['z'] = Bid.objects.values('model__name', 'delivery_date').annotate(month=TruncMonth('delivery_date')).values('model__name', 'month').annotate(Sum('amount_psc'))
    z = Bid.objects.annotate(month=TruncMonth('delivery_date')).values('model__name', 'month').annotate(Sum('amount_psc')).order_by('month')
    z5 = Bid.objects.annotate(month=TruncMonth('delivery_date')).values('model__id', 'month').annotate(Sum('amount_psc'))
    z1 = z.values('month').annotate(Count('month')).values('month')
    args['z'] = z
    args['z1'] = z1
    args['z3'] = Bid.objects.values('model__name', 'delivery_date').annotate(Sum('amount_psc'))

    Temp.objects.all().delete()
    print('type =', type(z))
    print('z5 =', z5.values())
    for zzz in z5:
        print('zzz =', zzz)
        mdl = Model.objects.get(id=zzz['model__id'])
        Temp.objects.create(month=zzz['month'], model=mdl, amount=zzz['amount_psc__sum'])
        # Temp.objects.create(**zzz)

    month_overview = z.annotate(
        okt=Case(When(month__month=10, month__year=2016, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        nov=Case(When(month__month=11, month__year=2016, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        dec=Case(When(month__month=12, month__year=2016, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        jan=Case(When(month__month=1, month__year=2017, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        feb=Case(When(month__month=2, month__year=2017, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        mar=Case(When(month__month=3, month__year=2017, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        apr=Case(When(month__month=4, month__year=2017, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        may=Case(When(month__month=5, month__year=2017, then='amount_psc__sum'), default=0, output_field=IntegerField()),
        june=Case(When(month__month=6, month__year=2017, then='amount_psc__sum'), default=0, output_field=IntegerField())
        ).order_by('month') #.values_list('month', 'model__name', 'okt', 'nov', 'dec')
    print('month_overview =', month_overview)
    args['month_overview'] = month_overview

    # start dates
    year = 2016
    month = 9
    # end dates
    # cyear = datetime.date.today().year
    # cmonth = datetime.date.today().month
    cyear = 2017
    cmonth = 2
    d = []
    while year <= cyear:
        while (year < cyear and month <= 12) or (year == cyear and month <= cmonth):
            # sales = Bid.objects.filter(delivery_date__year=year, delivery_date__month=month).aggregate(Count('amount_psc'), Sum('amount_psc'))
            sales = Temp.objects.filter(month__year=year, month__month=month).values('model__name', 'month').annotate(Sum('amount')) #.aggregate(Count('amount'), Sum('amount'))
            print('sales =', sales)
            # d.append({
            #     'year': year,
            #     'month': month,
            #     # 'sales': sales['amount_psc__count'] or 0,
            #     'sales': sales['amount__count'] or 0,
            #     # 'value': decimal.Decim_psc__count'] or 0,
            #     'value': decimal.Decimal(sales['amount__sum'] or 0),
            # })
            print('year =', year, 'cyear =', cyear, 'month =', month, 'cmonth =', cmonth)
            print('d =', d)
            month += 1
        month = 1
        year += 1

    # select sum(amount_psc) as 'Aug' from products_bid where model_id = 8 and date='2016-10-08'
    # SELECT * FROM
    # (select sum(amount_psc) as 'Aug' from products_bid where model_id = 8 and date = '2016-10-08'),
    # (select sum(amount_psc) as 'Sep' from products_bid where model_id = 8 and date = '2016-10-09'),
    # (select sum(amount_psc) as 'Okt' from products_bid where model_id = 8 and date = '2016-10-30')
    # products_bid
    # ------------
    # SELECT * FROM
    # (select sum(amount) as 'Aug' from products_temp where model_id = 9 and month = '2016-10-01'),
    # (select sum(amount) as 'Sep' from products_temp where model_id = 9 and month = '2016-11-01'),
    # (select sum(amount) as 'Okt' from products_temp where model_id = 9 and month = '2016-12-01')
    # products_temp

    args['d'] = d

    # bid = Bid.objects.filter()
    # print(bid.product)

    return render_to_response('selling.html', args)

@login_required
def add_bid(request):
    args = {}
    args.update(csrf(request))
    args['form'] = BidForm()

    # form = BidForm(initial={'color': '333'})

    if request.POST:
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save()
            compositions = Composition.objects.filter(model=bid.model)
            for composition in compositions:
                print('composition =', composition.name)
                amount = composition.total_expense * bid.amount_psc
                print('amount =', amount)
                BidComposition.objects.create(bid=bid, product=composition.model.product, model=composition.model ,composition=composition, amount=amount)
            return redirect('/')
        else:
            args['form'] = form

    return render_to_response('add_bid.html', args)

@login_required
def designer(request):
    args = {}
    args.update(csrf(request))
    args['compositions'] = Composition.objects.all()

    z = Bid.objects.annotate(month=TruncMonth('delivery_date')).values('model__name', 'month').annotate(Sum('amount_psc')).order_by('month')
    # z = BidComposition.objects.annotate(month=TruncMonth('bid__delivery_date')).values('model__name', 'month').annotate(Sum('bid__amount_psc')).order_by('month')
        #.values('model__name', 'month')
        #.annotate(Sum('amount_psc')).order_by('month')
    args['z'] = z
    print('z =', z.values())

    z1 = BidComposition.objects.annotate(month=TruncMonth('bid__delivery_date')).values('composition__name', 'month').annotate(Sum('amount')).order_by('month')
        #.values('model__name', 'month').annotate(Sum('bid__amount_psc')).order_by('month')
    args['z1'] = z1
    print('z1 =', z1.values())

    return render_to_response('designer.html', args)

@login_required
def add_designer(request):
    args = {}
    args.update(csrf(request))
    args['form'] = CompositionForm()

    if request.POST:
        form = CompositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/designer/')
        else:
            args['form'] = form

    return render_to_response('add_designer.html', args)

@login_required
def technologist(request):
    args = {}
    args.update(csrf(request))
    args['rawmaterials'] = Rawmaterial.objects.all()

    z1 = BidComposition.objects.annotate(month=TruncMonth('bid__delivery_date')).values('composition__name', 'month').annotate(Sum('amount')).order_by('month')
        #.values('model__name', 'month').annotate(Sum('bid__amount_psc')).order_by('month')
    args['z1'] = z1
    print('z1 =', z1.values())

    z2 = BidComposition.objects.filter(composition__ismanufacture=1).annotate(month=TruncMonth('bid__delivery_date')).values('composition', 'composition__name', 'month').annotate(Sum('amount')).order_by('month')
    # z2 = BidComposition.objects.filter(composition__ismanufacture=1).annotate(month=TruncMonth('bid__delivery_date')).values('composition__rawmaterial__name', 'month').annotate(Sum('amount')).order_by('month')
    print('type z2 =', type(z2))
    args['z2'] = z2
    print('z2 =', z2.values())
    print('z2 =', z2)

    for zzz in z2:
        rm = Rawmaterial.objects.filter(composition=zzz['composition'])
        print('zzz =', zzz['composition'])
        print('rm =', rm.values())

    print(BidComposition.objects.filter(composition__ismanufacture=1).filter(composition__rawmaterial=1))

    #!!!!!!!!!!!!!!!
    print(BidComposition.objects.filter(composition__ismanufacture=1).annotate(month=TruncMonth('bid__delivery_date')).values(
        'composition__rawmaterial__name', 'month').annotate(Sum('composition__rawmaterial__rm_profile')).order_by('month'))
    #!!!!!!!!!!!!!!!

    return render_to_response('technologist.html', args)

@login_required
def add_technologist(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RawmaterialForm()

    if request.POST:
        form = RawmaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/technologist/')
        else:
            args['form'] = form

    return render_to_response('add_technologist.html', args)
