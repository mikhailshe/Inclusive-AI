from settings.settings import DEBUG, env

"""
Настройки электронной почты для Django

Компонент отвечает за:
1. Настройку отправки электронной почты
2. Конфигурацию SMTP-серверов
3. Шаблоны и форматы писем
4. Мониторинг и ограничения для email
"""

# --------------------- ОСНОВНЫЕ НАСТРОЙКИ EMAIL -----------------------

# Адрес электронной почты отправителя по умолчанию
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='noreply@example.com')

# Адрес электронной почты для административных сообщений
SERVER_EMAIL = env('DEFAULT_FROM_EMAIL', default='server@example.com')

# Email-адреса администраторов
ADMINS = env.list(
    'ADMINS',
    default=[
        ("Admin Name", "admin@example.com"),
    ]
)


# Email-адреса менеджеров
MANAGERS = ADMINS

# ---------------------- НАСТРОЙКИ BACKEND EMAIL -----------------------

# Выбор бэкенда для отправки email
# Поддерживаемые значения:
# 'django.core.mail.backends.smtp.EmailBackend' - отправка через SMTP
# 'django.core.mail.backends.console.EmailBackend' - вывод в консоль
# 'django.core.mail.backends.filebased.EmailBackend' - запись в файлы
# 'django.core.mail.backends.locmem.EmailBackend' - хранение в памяти
# 'django.core.mail.backends.dummy.EmailBackend' - подавление отправки
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    

# -------------------------- НАСТРОЙКИ SMTP ----------------------------

# Хост SMTP-сервера
EMAIL_HOST = env('EMAIL_HOST', default='smtp.example.com')

# Порт SMTP-сервера
EMAIL_PORT = env.int('EMAIL_PORT', default=587) 

# Имя пользователя для аутентификации на SMTP-сервере
EMAIL_HOST_USER =  env('EMAIL_HOST_USER', default='')

# Пароль для аутентификации на SMTP-сервере
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

# Использовать TLS для защиты соединения
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)

# Использовать SSL для защиты соединения
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)

# Таймаут соединения в секундах
EMAIL_TIMEOUT = 30


# -------------------- НАСТРОЙКИ ДЛЯ ТЕСТИРОВАНИЯ ----------------------

# Префикс для тем писем в тестовом режиме
EMAIL_SUBJECT_PREFIX = '[TEST] '


# --------------------- НАСТРОЙКИ ШАБЛОНОВ EMAIL -----------------------

# Путь к шаблонам email
EMAIL_TEMPLATES_DIR = 'templates/email'

# Использовать HTML-шаблоны для писем
EMAIL_USE_HTML_TEMPLATES = True

# Автоматически создавать текстовую версию для HTML-писем
EMAIL_AUTO_GENERATE_TEXT = True


# ----------------------- НАСТРОЙКИ ОГРАНИЧЕНИЙ ------------------------

# Максимальное количество писем в час для одного пользователя
EMAIL_HOURLY_USER_LIMIT = 10

# Максимальное количество писем в день для всей системы
EMAIL_DAILY_SYSTEM_LIMIT = 10000

# Таймаут между отправками писем для одного пользователя (в секундах)
EMAIL_USER_TIMEOUT = 60

# ---------------- НАСТРОЙКИ ОТСЛЕЖИВАНИЯ И АНАЛИТИКИ ------------------

# Включить отслеживание открытий писем
EMAIL_TRACK_OPENS = False

# Включить отслеживание переходов по ссылкам
EMAIL_TRACK_CLICKS = False


# ------------------ НАСТРОЙКИ ДЛЯ МАССОВЫХ РАССЫЛОК -------------------

# Максимальное количество получателей в одном письме (для рассылок)
EMAIL_MAX_RECIPIENTS = 50

# Скрывать получателей при массовой рассылке (использовать BCC)
EMAIL_USE_BCC_FOR_MASS_EMAILS = True


# -------------------- НАСТРОЙКИ ФАЙЛОВЫХ ВЛОЖЕНИЙ ---------------------

# Максимальный размер всех вложений в одном письме (в байтах)
EMAIL_MAX_ATTACHMENT_SIZE = 10 * 1024 * 1024  # 10MB

# Разрешенные типы файлов для вложений
EMAIL_ALLOWED_ATTACHMENT_TYPES = [
    'application/pdf',
    'image/jpeg',
    'image/png',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'text/plain',
]


# ----------------------- НАСТРОЙКИ ЛОГИРОВАНИЯ ------------------------

# Включить логирование email
EMAIL_LOGGING_ENABLED = True

# Уровень логирования email
EMAIL_LOGGING_LEVEL = 'INFO'

# Хранить историю отправленных писем в базе данных
EMAIL_STORE_HISTORY = True

# Срок хранения истории писем (в днях, 0 = бессрочно)
EMAIL_HISTORY_RETENTION = 90


# ---------------------- НАСТРОЙКИ БЕЗОПАСНОСТИ ------------------------

# Проверять SPF, DKIM и DMARC для домена отправителя
EMAIL_CHECK_SECURITY = True


# --------------- НАСТРОЙКИ ДЛЯ DJANGO-TEMPLATED-EMAIL -----------------

# Включить поддержку django-templated-email
EMAIL_USE_TEMPLATED_EMAIL = False
