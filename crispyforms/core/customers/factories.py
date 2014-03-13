# -*- coding: utf-8 -*-

import factory
import faker

import models


fake = faker.Faker()


def fake_username(*args):
    while True:
        names = fake.name().split()
        if len(names) is 2:
            name = names[0].lower()+'.'+names[1].lower()
            if not models.Customer.objects.filter(username=name).exists():
                break
    return name


class CustomerFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Customer

    username = factory.Sequence(fake_username)
    title = factory.Iterator(('MR', 'MRS', 'MS'), cycle=True)
    first_name = factory.LazyAttribute(lambda o: o.username.split('.')[0])
    last_name = factory.LazyAttribute(lambda o: o.username.split('.')[1])
    email = factory.LazyAttribute(lambda o: o.username+'@gmail.com')

