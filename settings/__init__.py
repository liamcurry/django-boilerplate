import os.path
from django.core.urlresolvers import reverse_lazy


_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
                        os.path.abspath(__file__))))
_path = lambda *a: os.path.join(_ROOT, *a)

ADMINS = MANAGERS = (
    # ('Your Name', 'your_email@example.com'),
)
ASSETS_AUTO_BUILD = True
ASSETS_CACHE = True
ASSETS_DEBUG = False
ASSETS_JINJA2_EXTENSIONS = ['jinja2.ext.i18n', ]
ASSETS_MANIFEST = 'cache'
ASSETS_UPDATER = None
ASSETS_URL_EXPIRE = True
ASSETS_VERSIONS = 'hash'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}
DEBUG = TEMPLATE_DEBUG = True
FIXTURES_DIR = (
    _path('fixtures'),
)
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
    'apps.{{ project_name }}',
    'apps.auth'
)
JINGO_EXCLUDE_APPS = ('debug_toolbar', 'admin')
JINJA_CONFIG = {
    'extensions': [
        'jinja2.ext.i18n',
        'webassets.ext.jinja2.AssetsExtension'
    ]
}
LANGUAGE_CODE = 'en-us'
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
LOGIN_URL = reverse_lazy('auth:login')
LOGOUT_URL = reverse_lazy('auth:logout')
MEDIA_ROOT = _path('media')
MEDIA_URL = '/media/'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'apps.{{ project_name }}.urls'
SECRET_KEY = '{{ secret_key }}'
SITE_ID = 1
STATIC_ROOT = _path('static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django_assets.finders.AssetsFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STYLUS_EXTRA_ARGS = ['--include-css', ]
STYLUS_EXTRA_PATHS = [_path('apps', '{{ project_name }}', 'static', 'styl'), ]
STYLUS_PLUGINS = ['nib', ]
TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'wsgi.application'

import jingo.monkey
jingo.monkey.patch()

from django_assets.env import get_env as get_assets_env
import jingo
jingo.env.assets_environment = get_assets_env()

try:
    from .local import *
except ImportError:
    pass
