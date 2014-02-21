# -*- coding: utf-8 -*-
# Copyright (c) 2011-2014 Polyconseil SAS. All rights reserved.

from django.contrib import admin

from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'creation_date', 'is_active')

admin.site.register(models.Customer, CustomerAdmin)
