# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('crispyforms.ops.register.views',
    url(r'^$', views.list_customers, name='list'),
    url(r'^create/$', views.create_or_edit_customer, name='create'),
    url(r'^edit/(?P<customer_id>\d+)$', views.create_or_edit_customer, name='edit'),
    url(r'^delete/(?P<customer_id>\d+)$', views.delete_customer, name='delete'),
)
