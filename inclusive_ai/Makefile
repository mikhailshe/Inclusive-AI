fixtures:
	uv run manage.py loaddata fixtures/subject.json

get-fixtures:
	uv run manage.py dumpdata common.Subject --indent 4 > fixtures/subject.json

migrate:
	uv run manage.py makemigrations
	uv run manage.py migrate

run:
	uv run manage.py runserver 0.0.0.0:8000

shell:
	uv run manage.py shell

collectstatic:
	uv run manage.py collectstatic

superuser:
	uv run manage.py createsuperuser
