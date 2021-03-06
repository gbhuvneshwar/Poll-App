"""
Dang settings for poll_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gy$5_(8coxw+!@262a*q*&f^s%beavjvfsvd%zy_7rceztluje'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.
# So set it to '*' from [] to match any host

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
)

THIRD_PARTY_APPS = ('easy_maps', 'cities_light', 'address',)

LOCAL_APPS = (
    'poll',
    'articles',
    'masterIt',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'poll_app.urls'

WSGI_APPLICATION = 'poll_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# sending e-mails setting
EMAIL_HOST = 'localhost'
EMAIL_PORT = 8000

#Absolute file system part to the directory that will hold user uploaded files.
MEDIA_ROOT = '/home/shaifali/poll_app/static'

# Url that handle the media served from MEDIA_ROOT. Make sure to use a 
# trailing slash.
MEDIA_URL = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#Additional locations for static fiels
STATICFILES_DIRS =  (
    ('assets', '/home/shaifali/poll_app/static'),
    #always put absolute path and forward slashes
    )

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

LOGIN_URL = '/accounts/login/'

#for sending emails
EMAIL_USE_SSL = True
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'agrawalshaifali09@gmail.com'
EMAIL_HOST_PASSWORD = 'zqmyrgcwxozxxqzn'
DEFAULT_FROM_EMAIL = 'agrawalshaifali09@gmail.com'
DEFAULT_TO_EMAIL = 'agrawalshaifali09@gmail.com'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'