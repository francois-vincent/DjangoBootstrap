# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from django import http
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from core.customers import models as customer_models
from forms import CustomerForm


@login_required
def list_customers(request):
    query = request.GET.get('q', None)
    customers = customer_models.Customer.objects.search(query)
    return render(request, 'register/list.html', {'query': query, 'customers': customers})


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
        if customer:
            messages.info(request, _(u'Customer <strong>%s</strong> modified !') % customer)
        else:
            data = form.cleaned_data
            messages.info(request, _(u'New customer <strong>%s (%s %s)</strong> created !') %
                   (data['username'], data['first_name'], data['last_name']))
        return redirect('register:list')
    return render(request, 'register/edit.html', {'form': form, 'customer': customer})


@login_required
def delete_customer(request, customer_id):
    next = request.REQUEST.get('next', None) or request.META.get('HTTP_REFERER', None) or '/'
    response = http.HttpResponseRedirect(next)

    try:
        customer = customer_models.Customer.objects.get(pk=customer_id)
        customer.set_inactive()
        messages.info(request, _(u'Customer <strong>%s</strong> deleted !') % customer)
    except customer_models.Customer.DoesNotExist:
        messages.warning(request, _(u'Could not delete customer.'))

    return response
