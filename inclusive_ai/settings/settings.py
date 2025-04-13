import os
from pathlib import Path

import environ
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from split_settings.tools import include


# ------------------------ PROJECT DIRECTORIES -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = [BASE_DIR / 'locale']
LOGS_DIR = BASE_DIR / 'logs'
MEDIA_ROOT = BASE_DIR / 'uploads'


# ------------------------------ ENVIRON -------------------------------
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# ------------------------- SECURITY SETTINGS --------------------------
allowed_hosts = env.list('ALLOWED_HOSTS', default=[])
ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] + allowed_hosts


# -------------------------- DEBUG SETTINGS ----------------------------
DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = env.bool('TEMPLATE_DEBUG', default=False)


# --------------------------- SITE SETTINGS ----------------------------
SITE_ID = 1


# -------------------------- WSGI SETTINGS -----------------------------
WSGI_APPLICATION = 'settings.wsgi.application'


# -------------------------- URL SETTINGS ------------------------------
ADMIN_MEDIA_PREFIX = '/media/dev/admin//'
MEDIA_URL = '/media/'
ROOT_URLCONF = 'settings.urls'
STATIC_URL = '/static/'


# --------------------------- AUTH SETTINGS ----------------------------
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',]


# ------------------------ MIDDLEWARE SETTINGS -------------------------
MIDDLEWARE = [
    # ------------------ DJANGO -------------------
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


# ------------------------- TEMPLATE SETTINGS --------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # ------------------ DJANGO -------------------
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
            ],
        },
    },
]

# ---------------------------- STATICFILES -----------------------------
# Механизмы для поиска статических файлов
STATICFILES_FINDERS = (
    # Поиск в директориях, указанных в STATICFILES_DIRS
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # Поиск в поддиректории static каждого приложения
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Класс хранилища для статических файлов
# ManifestStaticFilesStorage добавляет хэш к именам
# файлов для инвалидации кэша
STATICFILES_STORAGE = ManifestStaticFilesStorage

if DEBUG:
    STATIC_DIR = BASE_DIR / 'static'
    STATICFILES_DIRS = [STATIC_DIR]
else:
    STATIC_ROOT = BASE_DIR / 'static'

USE_DJANGO_JQUERY = True


# ---------------------------- LLM & PROXY -----------------------------
AI_PROXY = env.list('AI_PROXY', default='')
ANTHROPIC_API_KEY = env.list('ANTHROPIC_API_KEY', default='default')


# -------------------------- INSTALLED APPS ----------------------------
INSTALLED_APPS = [
    # ------------------ DJANGO -------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    # ------------------ OTHER --------------------
    'allauth',
    'allauth.account',
    'sorl.thumbnail',

    # ----------------- PROJECT -------------------
    'apps.pages',
    'apps.pears',
]


# ------------------------ ADDITIONAL SETTINGS -------------------------
include(
    # ----------------- SECURITY ------------------
    'components/security/base.py',
    'components/security/content_security.py',
    'components/security/cors.py',
    'components/security/csrf.py',
    'components/security/orm_security.py',
    'components/security/session.py',
    'components/security/throttling.py',

    # --------------- PERFORMANCE -----------------
    'components/performance/caches.py',
    'components/performance/compression.py',

    # ----------------- DATABASE ------------------
    'components/database/sqlite.py',
    'components/database/postgresql.py',

    # -------------- AUTHENTICATION ---------------
    'components/authentication/account.py',

    # ----------- INTERNATIONALIZATION ------------
    'components/internationalization/base.py',
)
