"""
Django settings for RestaurantsProject project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'PLEASEGENERATEDJANGOSECRETKEY'

# SECURITY WARNING: don't run with debug turned on in production!
# En cas de tenir-ho activat mostra arxius estàtics sense haver de montar un nginx o un django-storages.
# Desactivar-ho reforça la seguretat, ja que sino mostra el codi i totes les rutes d'accès del nostre lloc web.
DEBUG = False

## Hosts Permesos
ALLOWED_HOSTS = ['*']

# Application definition

# Aplicacions instal·lades al projecte
INSTALLED_APPS = [
    'web_restaurants',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'django.contrib.postgres',
    'registration',
    'django_countries',
    'bootstrap4'
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

ROOT_URLCONF = 'RestaurantsProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'RestaurantsProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


### Database (local)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

DEFAULT_CHARSET = 'utf-8'

LANGUAGE_CODE = 'ca'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# Media Root

MEDIA_ROOT = os.path.join(BASE_DIR, 'web_restaurants/media/')
MEDIA_URL = '/media/'

## Django Registration Settings

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

## Redirecció en haver fet el login. (Si no s'indica el contrari)
LOGIN_REDIRECT_URL = 'home'

## Lloc Web que s'empra (només hi ha 1)
SITE_ID = 1

## Formulari de registre que ha d'emprar
REGISTRATION_FORM = 'web_restaurants.forms.RegistrationForm'

## Model d'usuari que ha d'emprar
AUTH_USER_MODEL = 'web_restaurants.Profile'

## Configuració Email
## El host és un contenidor Docker
EMAIL_HOST = os.environ.get('SMTP_HOST', '')

## Usuari i contrasenya del host SMTP
EMAIL_HOST_USER = os.environ.get('SMTP_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('SMTP_PASS', '')

## Ports i ús de TLS (no s'empra)
EMAIL_PORT = os.environ.get('SMTP_PORT', 25)
EMAIL_USE_TLS = os.environ.get('SMTP_USE_TLS', 'False')

## Backend de l'Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

## Email d'enviament de correus
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')

## Fa que no s'esperi un template HTML com a Email d'activació.
## En aquest cas empram "templates/activation_email.txt"
REGISTRATION_EMAIL_HTML = False

## Afegeix capçalera https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

## Maps API key
GOOGLE_MAPS_API = os.environ.get('GMAPS_API', '')

## Configuració caché Redis

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = os.environ.get('REDIS_DB', 1)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": ("redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}").format(REDIS_HOST=REDIS_HOST, REDIS_PORT=REDIS_PORT ,REDIS_DB=REDIS_DB)
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
