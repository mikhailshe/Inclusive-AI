"""
Настройки сжатия HTTP-ответов для Django

Компонент отвечает за:
1. Сжатие HTTP-ответов (gzip, brotli)
2. Оптимизацию передачи данных между сервером и клиентом
3. Настройки уровней сжатия и порогов размера файлов
"""

# ------------------ НАСТРОЙКИ GZIP -------------------

# Минимальный размер ответа для сжатия (в байтах)
GZIP_MIN_LENGTH = 200

# ------------------ НАСТРОЙКИ BROTLI -------------------

# Уровень сжатия Brotli (от 0 до 11, где 11 - максимальное сжатие)
BROTLI_LEVEL = 6

# ------------------ НАСТРОЙКИ DEFLATE -------------------

# Уровень сжатия Deflate (от 1 до 9, где 9 - максимальное сжатие)
DEFLATE_LEVEL = 6

# ------------------ ИСКЛЮЧЕНИЯ ИЗ СЖАТИЯ -------------------

# Список путей URL, которые не должны сжиматься
COMPRESSION_EXEMPT_PATHS = []

# Список типов контента, которые не должны сжиматься
COMPRESSION_EXEMPT_CONTENT_TYPES = []

# ------------------ ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ ОПТИМИЗАЦИИ -------------------

# Предпочтительные механизмы сжатия в порядке приоритета
CONTENT_ENCODING_PREFERENCE = ['gzip', 'deflate']

# Добавляем Brotli если он доступен
try:
    import brotli  # noqa
    CONTENT_ENCODING_PREFERENCE.insert(0, 'br')
except ImportError:
    pass

# ------------------ НАСТРОЙКИ КЭШИРОВАНИЯ СЖАТЫХ ОТВЕТОВ -------------------

# Время жизни сжатых ответов в кэше (в секундах)
COMPRESSED_RESPONSE_CACHE_TIMEOUT = 86400  # 1 день

# Использовать отдельный кэш для сжатых ответов
USE_SEPARATE_COMPRESSION_CACHE = False

# Псевдоним кэша для сжатых ответов
COMPRESSION_CACHE_ALIAS = "compression_cache"

# ------------------ НАСТРОЙКИ ДЛЯ ПРОКСИ-СЕРВЕРОВ -------------------

# Учитывать заголовок X-Forwarded-Proto
USE_X_FORWARDED_HOST = False

# Учитывать заголовок X-Forwarded-For
USE_X_FORWARDED_FOR = False

# ------------------ НАСТРОЙКИ СТАТИЧЕСКОГО СЖАТИЯ -------------------

# Включить предварительное сжатие статических файлов
STATIC_PRECOMPRESSION_ENABLED = False

# Алгоритмы для предварительного сжатия
STATIC_PRECOMPRESSION_ALGORITHMS = ["gzip", "brotli"]

# Минимальный размер файла для предварительного сжатия (в байтах)
STATIC_PRECOMPRESSION_MIN_SIZE = 1024  # 1KB

# Типы файлов для предварительного сжатия
STATIC_PRECOMPRESSION_CONTENT_TYPES = [
    "text/html",
    "text/css",
    "text/javascript",
    "application/javascript",
    "application/json",
    "image/svg+xml"
]

# ------------------ НАСТРОЙКИ ПРОИЗВОДИТЕЛЬНОСТИ СЖАТИЯ -------------------

# Максимальный размер ответа для сжатия (в байтах)
COMPRESSION_MAX_SIZE = 10 * 1024 * 1024  # 10MB