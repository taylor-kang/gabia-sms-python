# assert warnings are enabled
import os
import warnings


warnings.simplefilter('ignore', Warning)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
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
    'SENDER': '01000000000',
    'API_ID': 'test_api_id',
    'API_KEY': 'test_api_key'
}
