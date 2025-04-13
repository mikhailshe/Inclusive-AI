"""
Настройки безопасности Django

Компонент отвечает за:
1. Настройки защиты от XSS, CSRF и других атак
2. Конфигурацию HTTPS и SSL
3. Настройки паролей и их хэширования
4. Настройки доступа к сайту
"""
from settings.settings import env


SECRET_KEY=env.str('SECRET_KEY')


# ----------------- НАСТРОЙКИ ЗАЩИТЫ HTTP-ЗАГОЛОВКОВ -------------------

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=31536000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=True)

# Защита от атак на основе Content-Type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Защита от XSS-атак в старых браузерах
SECURE_BROWSER_XSS_FILTER = True

# Перенаправление с HTTP на HTTPS
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)

# Указывает, как определить, что запрос пришел
# через HTTPS, при работе за прокси
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Отключение предупреждения о Referrer-Policy
SILENCED_SYSTEM_CHECKS = ['security.W022']


# ------------------- НАСТРОЙКИ ХЭШИРОВАНИЯ ПАРОЛЕЙ --------------------

# Алгоритмы хэширования паролей (в порядке приоритета)
PASSWORD_HASHERS = [
    # PBKDF2 с SHA-256 - надежный алгоритм, доступный по умолчанию
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    # PBKDF2 с SHA-1 - для совместимости
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    # Argon2 - рекомендуемый алгоритм (требует argon2-cffi)
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    # BCrypt - еще один хороший алгоритм (требует bcrypt)
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]


# ------------------------- ВАЛИДАЦИЯ ПАРОЛЕЙ --------------------------

# Минимальная длина пароля
MIN_PASSWORD_LENGTH = 6

# Валидаторы пароля проверяют его надежность
AUTH_PASSWORD_VALIDATORS = [
    # Проверка схожести с данными пользователя
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},

    # Проверка минимальной длины
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': MIN_PASSWORD_LENGTH}
    },

    # Проверка на распространенные пароли
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},

    # Проверка на числовой пароль
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
