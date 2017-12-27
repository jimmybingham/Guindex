"""
Django settings for GuindexProject project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import secrets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Enable timezone support
USE_TZ = True

ALLOWED_HOSTS = ['45.79.148.4', 'guindex.ie', 'www.guindex.ie', '127.0.0.1', '172.28.5.22', '172.28.4.151']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'UserProfile',
    'Guindex',
    'TelegramUser',
    'GuindexUser',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'GuindexProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "UserProfile/templates"),
                 os.path.join(BASE_DIR, "UserProfile/templates/modals"),
                 os.path.join(BASE_DIR, "UserProfile/templates/emails"),
                 os.path.join(BASE_DIR, "TelegramUser/templates"),
                 os.path.join(BASE_DIR, "TelegramUser/templates/emails"),
                 os.path.join(BASE_DIR, "Guindex/templates"),
                 os.path.join(BASE_DIR, "Guindex/templates/modals"),
                 os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'GuindexProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "CDN/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = secrets.EMAIL
EMAIL_HOST_PASSWORD = secrets.PASSWORD
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'UserProfileLogFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "/var/log/UserProfile.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'TelegramUserLogFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "/var/log/TelegramUser.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'GuindexLogFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "/var/log/Guindex.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'GuindexStatsLogFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "/var/log/GuindexStats.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'GuindexAlertsLogFile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "/var/log/GuindexAlerts.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'UserProfile': {
            'handlers': ['UserProfileLogFile'],
            'propogate': True,
            'level': 'DEBUG',
        },
        'TelegramUser': {
            'handlers': ['TelegramUserLogFile'],
            'propogate': True,
            'level': 'DEBUG',
        },
        'Guindex': {
            'handlers': ['GuindexLogFile'],
            'propogate': True,
            'level': 'DEBUG',
        },
        'GuindexStats': {
            'handlers': ['GuindexStatsLogFile'],
            'propogate': True,
            'level': 'DEBUG',
        },
        'GuindexAlerts': {
            'handlers': ['GuindexAlertsLogFile'],
            'propogate': True,
            'level': 'DEBUG',
        },
    }
}

# Telegram API
BOT_HTTP_API_TOKEN = secrets.BOT_HTTP_API_TOKEN
