# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from crispyforms.core.customers import models as customers_model

from core.customers import models as customer_models
from forms import CustomerForm


@login_required
def list_customers(request):
    customers = customers_model.Customer.objects.all()
    return render(request, 'register/list.html', {'customers': customers})


@login_required
def create_or_edit_customer(request, customer_id=None):
    if customer_id:
        customer = get_object_or_404(customer_models.Customer, pk=customer_id)
        intro = _(u'Edit customer then save changes')
        submit = _(u'Save changes')
    else:
        customer = None
        intro = _(u'Enter new customer then submit')
        submit = _(u'Submit')

    form = CustomerForm(request.POST or None, instance=customer, intro=intro, submit=submit)
    if form.is_valid():
        form.save()
        return redirect('register:list')
    return render(request, 'register/edit.html', {'form': form, 'customer': customer})
