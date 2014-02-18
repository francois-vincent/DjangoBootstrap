# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from django import http
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.utils import translation

from forms import AuthenticateForm


def home(request):
    return render(request, 'home.html', {})


def logout_view(request, response=None):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    if not response:
        response = http.HttpResponseRedirect(next)

    logout(request)
    return response


def set_language(request, lang_code, response=None):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    if not response:
        response = http.HttpResponseRedirect(next)

    if lang_code and translation.check_for_language(lang_code):
        request.session['django_language'] = lang_code

    return response


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next = request.REQUEST.get('next', None)
                return http.HttpResponseRedirect(next)
            else:
                msg = u"Oops, this user is not active !"
                messages.warning(request, msg)
        else:
            msg = u"Oops, the Username / password pair does not match !"
            messages.warning(request, msg)

    return render(request, 'common/login.html', {'form': AuthenticateForm(request.POST or None)})
