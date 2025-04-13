FROM python:3.12-slim


# ------------------------------ System --------------------------------
RUN apt-get update
RUN apt-get install -y curl build-essential libpq-dev
ENV PATH="/root/.local/bin:$PATH"


# ------------------------------ Project -------------------------------
WORKDIR /srv/inclusive_ai

COPY inclusive_ai/ ./
COPY inclusive_ai/env.example .env

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

RUN uv venv
RUN make migrate

# RUN make collectstatic

CMD make run
