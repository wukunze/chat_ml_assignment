"""
Django settings for cse_site project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import braintree


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6%9d=wpq7&86&j9f(&*tl&e14aan*7k2_xup5*9#x6gjmov%(8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add our application
    'ubs_project.apps.UbsProjectConfig', # This object was created for us in /ubs_project/apps.py
    'bootstrap4',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cse_site.urls'

#  APP_DIRS = True  every application of django will automaticilly find template directory itself to load VIEW
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cse_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


#  MySQL 5.6  must >= 5.6
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ubs_system',
        'USER': 'root',# chat_ml, root
        'PASSWORD': '123',#cse6324team5, root
        'HOST': '127.0.0.1', #midgard.ddns.net ,127.0.0.1f
        'PORT': '3306',
    }
}

# 'ENGIN':  'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.dbK.backends.mysql'，or   'django.db.backends.oracle'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Set server time zone to Central Standard Time (Arlington time)
TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'cse_site/media')

LOGIN_REDIRECT_URL = "home"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_HOST_USER = '495228683@qq.com'
EMAIL_HOST_PASSWORD = 'hfntapejhhgtcabb'

BRAINTREE_MERCHANT_ID = 'tnpvv6qj3pwfgsjp' #Merchant ID
BRAINTREE_PUBLIC_KEY = 'bjvv9njny2j2hfm3' # Public Key
BRAINTREE_PRIVATE_KEY = '09f995beee171c98a52025f912914cac' # Private key
braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)
