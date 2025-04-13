"""
Настройки кэширования Django

Компонент отвечает за:
1. Конфигурацию бэкендов кэширования
2. Настройки кэша для шаблонов и middleware
3. Определение параметров хранения кэшированных данных
"""

from settings.settings import DEBUG

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ КЭША -------------------

""" Бэкенд кэширования
Django поддерживает несколько типов бэкендов для кэширования:
1. 'django.core.cache.backends.db.DatabaseCache' - кэширование в БД
2. 'django.core.cache.backends.file.FileBasedCache' - файловое кэширование
3. 'django.core.cache.backends.locmem.LocMemCache' - кэширование в памяти
4. 'django.core.cache.backends.dummy.DummyCache' - фиктивный кэш
5. 'django.core.cache.backends.memcached.PyMemcacheCache' - Memcached
6. 'django.core.cache.backends.memcached.PyLibMCCache' - Memcached
7. 'django.core.cache.backends.redis.RedisCache' - Redis
"""
CACHE_BACKEND = "django.core.cache.backends.locmem.LocMemCache"

# Расположение кэша
CACHE_LOCATION = "unique-snowflake"

# Время жизни кэшированных данных (в секундах)
CACHE_TIMEOUT = 300  # 5 минут

# Префикс ключей кэша
CACHE_KEY_PREFIX = "django_cache"

# Основные настройки кэша
CACHES = {
    "default": {
        "BACKEND": CACHE_BACKEND,
        "LOCATION": CACHE_LOCATION,
        "TIMEOUT": CACHE_TIMEOUT,
        "KEY_PREFIX": CACHE_KEY_PREFIX,
        "OPTIONS": {},
    }
}

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ ШАБЛОНОВ -------------------

# Настройки кэширования шаблонов
# Применяются только в продакшн-режиме (когда DEBUG = False)
TEMPLATE_LOADERS = None

if not DEBUG:  # Используем глобальную переменную DEBUG из settings.py
    TEMPLATE_LOADERS = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]

# ------------------ НАСТРОЙКИ MIDDLEWARE КЭШИРОВАНИЯ -------------------

# Кэширование на уровне сайта (требует middleware)
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 600  # 10 минут
CACHE_MIDDLEWARE_KEY_PREFIX = "site_cache"

# ------------------ НАСТРОЙКИ СЕССИЙ И КЭШИРОВАНИЯ -------------------

# Флаг для хранения сессий в кэше
SESSION_IN_CACHE = False

# При необходимости активировать кэширование сессий
if SESSION_IN_CACHE:
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
