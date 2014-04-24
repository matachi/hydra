"""
Django settings for hydra project.

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
SECRET_KEY = 'w!r_x!v0*np(o#)1za$v8ux1^3&q-i&(k#2aatj9+ct_n#oome'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'pipeline',

    'widget_tweaks',

    'django.contrib.sites',
    'django.contrib.comments',
    'django_comments_xtd',

    'hydra',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'hydra.urls'

WSGI_APPLICATION = 'hydra.wsgi.application'

# Required by django_comments_xtd
SITE_ID = 1

COMMENTS_APP = 'django_comments_xtd'

COMMENTS_XTD_MAX_THREAD_LEVEL = 5

COMMENTS_XTD_CONFIRM_EMAIL = False

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog/templates'),
    os.path.join(BASE_DIR, 'hydra/templates'),
)

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'templates/')
# )
