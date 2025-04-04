FROM python:3.12-slim

WORKDIR /app

COPY . /app/
RUN apt-get update && apt-get install -y curl python3-setuptools git && apt-get clean
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD cd inclusive_ai \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput \
    && gunicorn settings.wsgi -w 3 -b 0.0.0.0:8000
