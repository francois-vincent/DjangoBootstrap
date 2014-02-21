# -*- coding: utf-8 -*-

from django import http
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

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
                messages.info(request, _(u'Welcome back %s !') % user)
                return http.HttpResponseRedirect(next)
            else:
                messages.warning(request, _(u"Oops, this user is not active !"))
        else:
            messages.warning(request, _(u"Oops, the username / password pair does not match !"))

    return render(request, 'common/login.html', {'form': AuthenticateForm(request.POST or None)})
