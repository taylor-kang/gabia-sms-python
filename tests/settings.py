# assert warnings are enabled
import warnings


warnings.simplefilter('ignore', Warning)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
]

SITE_ID = 1
ROOT_URLCONF = 'core.urls'

SECRET_KEY = 'foobar'

GABIA_SMS_SETTINGS = {
    'SENDER': '',
    'API_ID': '',
    'API_KEY': ''
}
