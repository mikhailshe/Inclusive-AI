# Inclusive AI

**Inclusive AI** — MVP-платформа на Django для инклюзивного обучения детей с ОВЗ с использованием ИИ. Проект создан в рамках ВСОШ по информационной безопасности.

---

## Быстрый старт (локально)
### 1. Клонируем репозиторий
git clone https://github.com/your-name/inclusive-ai.git
cd inclusive-ai

### 2. Создаём .env
cp inclusive_ai/env.example inclusive_ai/.env

### 3 Устанавка uv
curl -LsSf https://astral.sh/uv/install.sh | sh

### 4. Создание виртуального окружения
uv venv

### 5. Запуск
make migrate
make run

---

## Запуск в Docker
### Сборка образа
docker build . -t inclusive-ai

### Запуск контейнера
docker run -p 8000:8000 inclusive-ai
## Лицензия
[MIT License](./LICENSE)
