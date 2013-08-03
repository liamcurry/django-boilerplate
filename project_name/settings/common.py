from os.path import dirname, abspath, join
from django.conf.global_settings import (TEMPLATE_LOADERS, STATICFILES_FINDERS,
                                         TEMPLATE_CONTEXT_PROCESSORS,
                                         MIDDLEWARE_CLASSES)
from django.core.urlresolvers import reverse_lazy


ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))


# custom


# general
ALLOWED_HOSTS = ['localhost', ]
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'djcelery',
    'storages',
    'south',
    'haystack',
    '{{ project_name }}.auth',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s "
                      "[%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(ROOT_PATH, 'logs', 'django.log'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'logfile', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    '{{ project_name }}.context_processors.google_analytics_key',
)
TEMPLATE_DIRS = (join(ROOT_PATH, '{{ project_name }}', 'templates'), )
SITE_ID = 1
INTERNAL_IPS = ('127.0.0.1', )
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# i18n stuff
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# urls
LOGIN_URL = reverse_lazy('auth:login')
LOGOUT_URL = reverse_lazy('auth:logout')
ROOT_URLCONF = '{{ project_name }}.urls'


# django-storages
AWS_STORAGE_BUCKET_NAME = '{{ project_name }}'
AWS_S3_URL_PROTOCOL = 'https:'
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
#AWS_S3_CUSTOM_DOMAIN = '{}.cloudfront.net'.format(AWS_STORAGE_BUCKET_NAME)


# ssl
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# static files
MEDIA_ROOT = join(ROOT_PATH, '_media')
MEDIA_URL = '/media/'
STATIC_ROOT = join(ROOT_PATH, '_public')
STATIC_URL = '/public/'
STATICFILES_DIRS = (
    join(ROOT_PATH, '{{ project_name }}', 'static'),
)


# celery
from datetime import timedelta
BROKER_URL = 'amqp://guest:guest@localhost:5672/'
CELERY_TIMEZONE = 'UTC'

# haystack
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 40
#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': '{{ project_name }}.utils.elasticsearch.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': '{{ project_name }}',
    },
}
ELASTICSEARCH_INDEX_SETTINGS = {
    "index": {
        "analysis": {
            "analyzer": {
                "synonym": {
                    "tokenizer": "whitespace",
                    "filter": ["synonym"]
                }
            },
            "filter": {
                "synonym": {
                    'type': 'synonym',
                    'synonyms_path': join(ROOT_PATH, 'config',
                                          'elasticsearch', 'synonym.txt')
                }
            }
        }
    }
}
ELASTICSEARCH_DEFAULT_ANALYZER = "snowball"


# Secret key
from uuid import uuid4
SECRET_KEY = uuid4()


# Jinja2
JINGO_EXCLUDE_APPS = ('debug_toolbar', 'admin')
TEMPLATE_LOADERS = ('jingo.Loader', ) + TEMPLATE_LOADERS
