# Django settings for crispyforms project.

from datetime import datetime
import os
import sys

from django.utils.translation import pgettext_lazy


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
CHECKOUT_DIR = os.path.abspath(os.path.dirname(ROOT_DIR))

sys.path.insert(1, ROOT_DIR)

SERVICE = 'ops'
assert SERVICE in ('core', 'ops'), "Invalide service %s" % SERVICE

# Name of the project (e.g GitHub repository)
PROJECT_NAME = 'crispytest'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Core applications = models and low-level control
CORE_APPS = (
    'core.customers',
)

# Control apps = high-level controls and API (management commands, ...)
CONTROL_APPS = (

)

# Operations applications = views
OPS_APPS = (
    'ops.common',
    'ops.register',
)

DJANGO_APPS = (
    # Contrib apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    # 3rd parties
    'south',
    'crispy_forms',
    'linaro_django_pagination',
)

if SERVICE == 'core':
    ROOT_URLCONF = None
    TEST_APPS = CORE_APPS

elif SERVICE == 'ops':
    ROOT_URLCONF = 'crispyforms.ops.urls'
    TEST_APPS = OPS_APPS

INSTALLED_APPS = CORE_APPS + CONTROL_APPS + OPS_APPS + DJANGO_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PROJECT_NAME,
        'USER': PROJECT_NAME,
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
}
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, 'static/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^+cr9v+(m3t_kv6bh96i2cl1=_h!d%^6s=sb@3$d2r%3%sxqst'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'crispyforms.wsgi.application'

if SERVICE == 'ops':
    TEMPLATE_DIRS = (
        os.path.join(ROOT_DIR, 'ops', 'templates'),
    )
else:
    TEMPLATE_DIRS = ()

LANGUAGES = (
    ('fr', pgettext_lazy('language', "French")),
    ('en', pgettext_lazy('language', "English")),
)

LOCALE_PATHS = (
    os.path.join(ROOT_DIR, 'locale'),
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'minimal': {
            'format': '%(levelname)s %(name)s: %(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'minimal',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(CHECKOUT_DIR, 'logs/%s_%s.log' % (PROJECT_NAME, datetime.now().date().isoformat())),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# crispy-forms settings
# ~~~~~~~~~~~~~~~~~~~~~

CRISPY_FAIL_SILENTLY = not DEBUG
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# linaro-pagination settings, see http://pythonhosted.org/linaro-django-pagination/usage.html#optional-settings
# ~~~~~~~~~~~~~~~~~~~~~

PAGINATION_DISPLAY_DISABLED_PREVIOUS_LINK = True
PAGINATION_DISPLAY_DISABLED_NEXT_LINK = True
