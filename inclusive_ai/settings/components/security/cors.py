"""
Настройки Cross-Origin Resource Sharing (CORS) для Django

Компонент отвечает за:
1. Конфигурацию доступа к API и ресурсам с других доменов
2. Настройки заголовков CORS для HTTP-ответов
3. Управление предварительными запросами (preflight requests)
4. Контроль доступа к куки и аутентификации при кросс-доменных запросах
"""
from settings.settings import DEBUG, env


# ------------------ ОСНОВНЫЕ НАСТРОЙКИ CORS -------------------

# Разрешить запросы со всех доменов
CORS_ALLOW_ALL_ORIGINS = env.bool('CORS_ALLOW_ALL_ORIGINS', default=False)

# Список доменов, с которых разрешены запросы
cors_allowed_origins = env.list('CORS_ALLOWED_ORIGINS', default=[])
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000'
    ] + cors_allowed_origins

# URL, для которых CORS включен
CORS_URLS_REGEX = r'^.*$'

# ------------------ НАСТРОЙКИ ЗАГОЛОВКОВ CORS -------------------

# Разрешить передачу учетных данных (cookies, HTTP-аутентификация)
CORS_ALLOW_CREDENTIALS = env.bool('CORS_ALLOW_CREDENTIALS', default=True)

# Список HTTP-методов, разрешенных для CORS-запросов
CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']

# Список HTTP-заголовков, разрешенных для CORS-запросов
CORS_ALLOW_HEADERS = [
    'accept', 'accept-encoding', 'authorization', 'content-type',
    'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with'
]

# Список HTTP-заголовков, которые будут доступны клиенту
CORS_EXPOSE_HEADERS = []

# ------------------ НАСТРОЙКИ PREFLIGHT ЗАПРОСОВ -------------------

# Срок действия результатов предварительных запросов (preflight) в секундах
CORS_PREFLIGHT_MAX_AGE = 86400  # 1 день

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ -------------------

# Добавлять заголовок Vary: Origin ко всем ответам
CORS_VARY_HEADER = True

# ------------------ ОТЛАДКА CORS -------------------

# Добавлять отладочную информацию в заголовки ответов
CORS_DEBUG = DEBUG

# ------------------ ПАРАМЕТРЫ ДЛЯ СПЕЦИФИЧНЫХ КЛИЕНТОВ -------------------

# Разрешить запросы с null-происхождением
CORS_ALLOW_NULL_ORIGIN = False
