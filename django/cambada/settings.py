"""
Django settings for cambada project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y@71^l7*zx*lr4&+(gbe%6v&v^x%ha1rt4(drqq-8bdncgax+='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['matheusmonego.pythonanywhere.com', 'localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'webpush',
    'frases_historicas'
)

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

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


ROOT_URLCONF = 'cambada.urls'

WSGI_APPLICATION = 'cambada.wsgi.application'


CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# WEBPUSH_SETTINGS = {
#     "VAPID_PUBLIC_KEY": "BFg1VdS8njeZur1aWfWxm6SXuqp60zBBmdNnMTYDYqNIkpeKQz0ab6WfVmMcOnDKWPTjgzfMPWyDffvmT9H8Pos",
#     "VAPID_PRIVATE_KEY":"i6DYrsERcT3mRuGq08v6TuIE75RZxaWSLuvlD26w6Hk",
#     "VAPID_ADMIN_EMAIL": "matheusdemicheli@gmail.com"
# }

WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "BDnic52EBWr9E4m6JVjDFjvHUzrXn3ybWz74XGFhjgw5oIh021fF1IxWQwt8-BsWLw6_7qpWGlNON9g_SADJtpg",
    "VAPID_PRIVATE_KEY":"ouAvOsmZFWk6fkDxK7a0TNKAnYBWlYoLi8M-ZYWnO_s",
    "VAPID_ADMIN_EMAIL": "matheusdemicheli@gmail.com"
}


# {
# "subject" : "mailto: <matheusdemicheli@gmail.com>",
# "publicKey" : "BFg1VdS8njeZur1aWfWxm6SXuqp60zBBmdNnMTYDYqNIkpeKQz0ab6WfVmMcOnDKWPTjgzfMPWyDffvmT9H8Pos",
# "privateKey" : "i6DYrsERcT3mRuGq08v6TuIE75RZxaWSLuvlD26w6Hk"
# }
