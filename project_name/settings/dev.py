from .common import *


ADMINS = MANAGERS = (('Admin', 'admin@site.com'), )
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password'
    }
}

TEMPLATE_DEBUG = DEBUG = True
SECRET_KEY = 'secret_key'

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += ('debug_toolbar', )


from . import monkey
