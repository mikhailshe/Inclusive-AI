from settings.settings import BASE_DIR, DEBUG, env


USE_SQLITE = env.bool('USE_SQLITE', default=True)

if USE_SQLITE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "TIME_ZONE": None,
            # Время (в секундах), в течение которого соединение с БД открыто
            "CONN_MAX_AGE": 0,  
            "OPTIONS": {
                # Таймаут подключения (секунды)
                "timeout": 20,  
            },
            "TEST": {
                "NAME": BASE_DIR / "test_db.sqlite3",
                # Используется, если необходимо "отзеркалить"
                # другую БД для тестов
                "MIRROR": None,
                "CHARSET": None,
                "COLLATION": None,
            },
            # Оборачивать ли каждый запрос в транзакцию
            "ATOMIC_REQUESTS": False,
            # Автоматически выполнять commit после каждого запроса
            "AUTOCOMMIT": True,
        }
    }

    # Проверка работоспособности соединений перед использованием (Django 4.2+)
    CONN_HEALTH_CHECKS = False  

    # Роутеры для перенаправления запросов между
    # несколькими БД, если необходимо
    DATABASE_ROUTERS = []  

    # Кастомные пути для модулей миграций
    MIGRATION_MODULES = {}
