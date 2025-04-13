"""
Настройки сессий Django

Компонент отвечает за:
1. Хранение и обработку сессий пользователей
2. Настройку безопасности сессионных куки
3. Настройку поведения сессий
4. Конфигурацию сериализации данных сессий
"""
from settings.settings import env


# ------------------ ХРАНЕНИЕ СЕССИЙ -------------------

# Выбор бэкенда для хранения сессий
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Если используется хранилище сессий на основе
# кэша, указывается используемый кэш
SESSION_CACHE_ALIAS = 'default'

# Если используется файловое хранилище сессий,
# задает каталог для хранения файлов сессий
SESSION_FILE_PATH = None

# Ограничение времени неактивности администратора (в секундах)
SESSION_IDLE_TIMEOUT = 1800  # 30 минут


# ------------------ НАСТРОЙКИ КУКИ СЕССИЙ -------------------

# Возраст сессионных файлов cookie в секундах (по умолчанию 2 недели)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14

# Домен, используемый для сессионных файлов cookie
SESSION_COOKIE_DOMAIN = env('SESSION_COOKIE_DOMAIN', default=None)

# HttpOnly флаг для сессионных куки
SESSION_COOKIE_HTTPONLY = True

# Имя куки для сессии
SESSION_COOKIE_NAME = 'sessionid'

# Путь, заданный для сессионных куки
SESSION_COOKIE_PATH = '/'

# SameSite флаг для сессионных куки
SESSION_COOKIE_SAMESITE = 'Lax'

# Secure флаг для сессионных куки
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=True)


# ------------------ ПОВЕДЕНИЕ СЕССИЙ -------------------

# Истечет ли срок действия сессии, когда пользователь закроет браузер
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Сохранять данные сессии при каждом запросе
SESSION_SAVE_EVERY_REQUEST = False


# ------------------ СЕРИАЛИЗАЦИЯ ДАННЫХ -------------------

# Класс сериализатора для данных сессии
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
