# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'ops.common.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/', 'ops.common.views.logout_view', name='logout'),
    url(r'^accounts/login/', 'ops.common.views.login_view', name='login'),
    url(r'^language/(?P<lang_code>[a-z]+)/$', 'ops.common.views.set_language', name='change_language'),

    url(r'^customers/', include('crispyforms.ops.register.urls', namespace='register', app_name='register')),
)
