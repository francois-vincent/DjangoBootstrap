# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


TITLE_CHOICES = (
    ('MR', _(u'Mr.')),
    ('MRS', _(u'Mrs.')),
    ('MS', _(u'Ms.')),
)


class CustomerManager(models.Manager):

    def active(self):
        return self.filter(is_active=True)

    def search(self, pattern):
        if pattern:
            return self.active().filter(
                models.Q(username__icontains=pattern) |
                models.Q(first_name__icontains=pattern) |
                models.Q(last_name__icontains=pattern),
            )
        return self.active()


class Customer(models.Model):
    username = models.CharField(_(u"username"), unique=True, max_length=32)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, blank=True)
    first_name = models.CharField(_(u"first name"), blank=True, max_length=32)
    last_name = models.CharField(_(u"last name"), blank=True, max_length=32)
    email = models.CharField(_(u"email"), max_length=64)
    creation_date = models.DateTimeField(_(u"Creation date"), default=timezone.now, editable=False)
    is_active = models.BooleanField(_(u'Active'), default=True)

    objects = CustomerManager()

    class Meta:
        verbose_name = _(u"customer")
        verbose_name_plural = _(u"customers")

    def __unicode__(self):
        if self.first_name:
            return u'%s (%s%s)' % (self.username, self.first_name, u' '+self.last_name if self.last_name else '')
        else:
            return self.username

    def friendly(self):
        return self.first_name if self.first_name else self.username

    def set_inactive(self):
        self.is_active = False
        self.save()
