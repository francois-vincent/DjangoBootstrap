# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from django.core.urlresolvers import reverse

from crispy_forms.layout import Layout, Fieldset, Submit, Button
from crispy_forms.bootstrap import FormActions, InlineRadios

from core.customers import models as customers_models
from utils.forms import BootstrapModelForm


class CustomerForm(BootstrapModelForm):

    def __init__(self, *args, **kwargs):
        intro = kwargs.pop('intro', None)
        submit = kwargs.pop('submit', None)
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Fieldset(
                intro,
                'username',
                'email',
                InlineRadios('title'),
                'first_name',
                'last_name',
            ),
            FormActions(
                Submit('save', submit),
                Button('cancel', 'Cancel', onclick="location.href='%s'" % reverse('register:list')),
            )
        )

    class Meta:
        model = customers_models.Customer
