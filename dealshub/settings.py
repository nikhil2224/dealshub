"""
Django settings for dealshub project.
"""

from pathlib import Path
import os
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-dealshub-secret-key-change-in-production-2024'

DEBUG = os.environ.get('VERCEL') != '1'

ALLOWED_HOSTS = ['*'] # Change this to your specific domain in production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'deals',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dealshub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'deals.context_processors.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'dealshub.wsgi.application'

# Database - SQLite (easy to switch to MySQL/PostgreSQL)
db_path = BASE_DIR / 'db.sqlite3'

# Vercel's filesystem is read-only. Copy the database to /tmp to allow SQLite to function.
if os.environ.get('VERCEL') == '1' or os.environ.get('VERCEL_ENV'):
    tmp_db_path = '/tmp/db.sqlite3'
    if os.path.exists(db_path) and not os.path.exists(tmp_db_path):
        shutil.copy2(db_path, tmp_db_path)
    db_path = tmp_db_path

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': db_path,
        'OPTIONS': {
            'timeout': 20,
        }
    }
}

# MySQL config (uncomment to use MySQL instead):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dealshub_db',
#         'USER': 'root',
#         'PASSWORD': 'your_password',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Email (configure for newsletter/contact)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
