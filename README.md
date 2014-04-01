# DjangoBootstrap

A simple Django project with Bootstrap, Crispyforms and a language selector.


## Quick Start

1. Create a virtualenv and enter it, then install requirements:
```
    pip install - r requirements.txt
```

2. Create a postgres database 'crispytest', then initialize it:
```
    python manage.py syncdb --all (define a superuser)
    python manage.py migrate --fake
```

3. Populate it via factory:
```
    python manage.py shell
    >>> from core.customers.factories import CustomerFactory
    >>> CustomerFactory.create_batch(100)
```

4. If you want to test ``django-reversion``:
```
    python manage.py createinitialrevisions
```

5. Then launch django dev server:
```
    python manage.py runserver
```

and open your browser on ``127.0.0.1:8000``
