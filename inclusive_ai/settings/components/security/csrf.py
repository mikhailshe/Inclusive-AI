"""
Настройки защиты от CSRF-атак в Django

Компонент отвечает за:
1. Конфигурацию CSRF-защиты
2. Настройки CSRF-токенов и их срока действия
3. Настройки доверенных источников
4. Параметры CSRF-cookie
"""
from settings.settings import env


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ CSRF -------------------

# Возраст CSRF-cookie в секундах (по умолчанию 1 год)
CSRF_COOKIE_AGE = 60 * 60 * 24 * 365

# Домен для CSRF-cookie
CSRF_COOKIE_DOMAIN = env('CSRF_COOKIE_DOMAIN', default=None)

# Путь для CSRF-cookie
CSRF_COOKIE_PATH = '/'

# Имя CSRF-cookie
CSRF_COOKIE_NAME = 'csrftoken'

# Имя заголовка для CSRF-токена
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'

# Установить флаг HttpOnly для CSRF-cookie
CSRF_COOKIE_HTTPONLY = False

# Установить флаг Secure для CSRF-cookie
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=True)

# SameSite флаг для CSRF-cookie
CSRF_COOKIE_SAMESITE = 'Lax'

# ------------------ ПРОВЕРКА РЕФЕРЕРА -------------------

# Требовать заголовок Referer для проверки CSRF
CSRF_REFERER_CHECK_ORIGIN = True

# ------------------ ДОВЕРЕННЫЕ ИСТОЧНИКИ -------------------

# Список доверенных источников для CSRF
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ -------------------

# Использовать CSRF с куки сессий
CSRF_USE_SESSIONS = False

# Сбрасывать CSRF-токен при выходе пользователя
CSRF_ROTATE_ON_LOGOUT = False

# ------------------ CSRF В AJAX-ЗАПРОСАХ -------------------

# Имя атрибута в HTML-формах для CSRF-токена
CSRF_FORM_FIELD_NAME = 'csrfmiddlewaretoken'

# ------------------ ОБРАБОТКА ОШИБОК CSRF -------------------

# Шаблон для страницы с ошибкой CSRF
CSRF_FAILURE_TEMPLATE = '403_csrf.html'

# View для обработки ошибок CSRF
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
