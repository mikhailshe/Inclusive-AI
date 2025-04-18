"""
Настройки ограничения запросов (throttling) для Django

Компонент отвечает за:
1. Ограничение частоты запросов от клиентов
2. Защиту от DoS-атак и брутфорса
3. Настройку приоритетов для различных типов запросов
"""


# -------------------- ОБЩИЕ НАСТРОЙКИ THROTTLING ----------------------

# Включить ограничение запросов
THROTTLING_ENABLED = True

# ------------- НАСТРОЙКИ ОГРАНИЧЕНИЯ ДЛЯ АУТЕНТИФИКАЦИИ ---------------

# Максимальное количество попыток входа в систему за указанный период
LOGIN_THROTTLE_RATE = 5  # попыток

# Период для подсчета попыток входа (в секундах)
LOGIN_THROTTLE_PERIOD = 300  # 5 минут

# Время блокировки после превышения лимита (в секундах)
LOGIN_THROTTLE_LOCKOUT_TIME = 1800  # 30 минут

# URL-адреса для ограничения частоты запросов при аутентификации
LOGIN_THROTTLE_URLS = [
    '/login/',
    '/admin/login/',
    '/api/auth/token/'
]

# ------------------- НАСТРОЙКИ ОГРАНИЧЕНИЯ ДЛЯ API --------------------

# Ограничение запросов API для анонимных
# пользователей (запросов в минуту)
API_THROTTLE_ANON_RATE = 60

# Ограничение запросов API для авторизованных
# пользователей (запросов в минуту)
API_THROTTLE_USER_RATE = 1000


# ------------------ НАСТРОЙКИ БУРСТА -------------------

# Максимальное количество запросов в бурсте
THROTTLE_BURST_RATE = 10


# --------------- НАСТРОЙКИ ХРАНЕНИЯ ДАННЫХ THROTTLING -----------------

# Бэкенд для хранения данных о запросах
THROTTLE_BACKEND = 'default'

# Префикс ключа для хранения данных ограничения запросов
THROTTLE_KEY_PREFIX = 'throttle'


# ------------- НАСТРОЙКИ ОТВЕТОВ ПРИ ПРЕВЫШЕНИИ ЛИМИТОВ ---------------

# HTTP код при превышении лимита ограничения запросов
THROTTLE_STATUS_CODE = 429  # Too Many Requests

# Время сброса лимита, указываемое в заголовке ответа (в секундах)
THROTTLE_RETRY_AFTER = 60


# ----------------- НАСТРОЙКИ БЕЛОГО И ЧЕРНОГО СПИСКА ------------------

# IP-адреса, на которые не распространяются ограничения (белый список)
THROTTLE_WHITELIST_IPS = []

# IP-адреса, которые полностью заблокированы (черный список)
THROTTLE_BLACKLIST_IPS = []


# -------------- НАСТРОЙКИ ОГРАНИЧЕНИЯ ПО ПОЛЬЗОВАТЕЛЯМ ----------------

# Группы пользователей, на которые не распространяются ограничения
THROTTLE_EXEMPT_GROUPS = ['admin', 'staff']


# ------------------- НАСТРОЙКИ ЗАЩИТЫ ОТ БРУТФОРСА --------------------

# Включить блокировку за множественные неудачные попытки доступа
BRUTEFORCE_PROTECTION_ENABLED = True

# Количество неудачных попыток до временной блокировки
BRUTEFORCE_MAX_ATTEMPTS = 5

# Время блокировки после превышения лимита
# неудачных попыток (в секундах)
BRUTEFORCE_LOCKOUT_TIME = 1800  # 30 минут

# Время сброса счетчика неудачных попыток (в секундах)
BRUTEFORCE_RESET_TIME = 86400  # 24 часа


# ----------------------- НАСТРОЙКИ ЛОГИРОВАНИЯ ------------------------

# Включить логирование превышения лимитов
THROTTLE_LOGGING_ENABLED = True

# Уровень логирования для превышения лимитов
THROTTLE_LOGGING_LEVEL = 'WARNING'
