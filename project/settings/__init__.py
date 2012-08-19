import os.path

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
                        os.path.abspath(__file__))))
_path = lambda *a: os.path.join(_ROOT, *a)

ADMINS = MANAGERS = (
  # ('Your Name', 'your_email@example.com'),
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.dev.db',
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
    'project.{{ project_name }}',
)
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
MEDIA_ROOT = ''
MEDIA_URL = ''
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'project.urls'
SECRET_KEY = '{{ secret_key }}'
SITE_ID = 1
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    _path('project', 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_DIRS = (
    _path('project', 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'project.wsgi.application'

try:
    from .local import *
except ImportError:
    pass
