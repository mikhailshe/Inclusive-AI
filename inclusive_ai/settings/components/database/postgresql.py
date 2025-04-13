from settings.settings import DEBUG, env


USE_PSQL = env.bool('USE_PSQL', default=False)

if USE_PSQL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": env('DB_POSTGRESQL_HOST', default='localhost'),
            "PORT": env('DB_POSTGRESQL_PORT', default='5432'),
            "NAME": env('DB_POSTGRESQL_NAME', default=''),
            "USER": env('DB_POSTGRESQL_USER', default=''),
            "PASSWORD": env('DB_POSTGRESQL_PASSWORD', default=''),
            "CONN_MAX_AGE": 60 * 10,  # 10 minutes
        }
    }

