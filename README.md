# Inclusive AI

**Inclusive AI** — MVP-платформа на Django для инклюзивного обучения детей с ОВЗ с использованием ИИ. Проект создан в рамках ВСОШ по информационной безопасности.

## Быстрый старт (локально)
### 1. Клонируем репозиторий
```bash
git clone https://github.com/your-name/inclusive-ai.git
cd inclusive-ai
```

### 2. Создаём `.env`
```bash
cp inclusive_ai/env.example inclusive_ai/.env
```

### 3 Устанавка `uv`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 4. Создание виртуального окружения
```bash
uv venv
```

### 5. Запуск
```bash
make migrate
make run
```

---

## Запуск в Docker
### Сборка образа
```bash
docker build . -t inclusive-ai
```

### Запуск контейнера
```bash
docker run -p 8000:8000 inclusive-ai
```

---

## Makefile команды
```makefile
make migrate       # Выполнить миграции
make run           # Запустить dev-сервер Django
make collectstatic # Собрать статику
make superuser     # Создать суперпользователя
```

## Лицензия
[MIT License](./LICENSE)
