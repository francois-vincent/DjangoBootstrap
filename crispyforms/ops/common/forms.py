# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import FormActions

from utils.forms import BootstrapForm

LANGUAGES_CHOICES = settings.LANGUAGES


class LanguageForm(forms.Form):
    language = forms.ChoiceField(choices=LANGUAGES_CHOICES, required=True)


class AuthenticateForm(BootstrapForm):
    username = forms.CharField(label=_(u'Username'), required=True)
    password = forms.CharField(label=_(u'Password'), required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(AuthenticateForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Fieldset(
                _(u'Please enter your credentials'),
                'username',
                'password',
            ),
            FormActions(
                Submit('save', u'Login'),
            )
        )
