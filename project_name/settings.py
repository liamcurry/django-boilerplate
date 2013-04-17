import os.path
from django.conf.global_settings import STATICFILES_FINDERS, TEMPLATE_LOADERS
from django.core.urlresolvers import reverse_lazy


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'django_assets',
    '{{ project_name }}',
    '{{ project_name }}.auth'
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
SECRET_KEY = '{{ secret_key }}'
SITE_ID = 1
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
INTERNAL_IPS = ['127.0.0.1', ]


# urls
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
ROOT_URLCONF = '{{ project_name }}.urls'


# staticfiles
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'


# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# jinja2
JINGO_EXCLUDE_APPS = ('debug_toolbar', 'admin')
JINJA_CONFIG = {
    'extensions': ['jinja2.ext.i18n', 'webassets.ext.jinja2.AssetsExtension']
}
TEMPLATE_LOADERS = ('jingo.Loader', ) + TEMPLATE_LOADERS


# webassets
ASSETS_AUTO_BUILD = True
ASSETS_CACHE = True
ASSETS_DEBUG = False
ASSETS_JINJA2_EXTENSIONS = ['jinja2.ext.i18n', ]
ASSETS_MANIFEST = 'cache'
ASSETS_UPDATER = None
ASSETS_URL_EXPIRE = True
ASSETS_VERSIONS = 'hash'
STYLUS_EXTRA_ARGS = ['--include-css', ]
STYLUS_EXTRA_PATHS = [
    os.path.join(ROOT_PATH, '{{ project_name }}', 'stylus'),
]
STYLUS_PLUGINS = ['nib', ]
STATICFILES_FINDERS += ('django_assets.finders.AssetsFinder', )


try:
    from .settings_local import *
except ImportError:
    pass


import jingo
import jingo.monkey
from django_assets.env import get_env as get_assets_env
jingo.monkey.patch()
jingo.env.assets_environment = get_assets_env()
