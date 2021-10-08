deps:
	apt-get update
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py collectstatic

lint:
	isort backend
	flake8 backend

test:
	cd backend && pytest

coverage:
	cd backend && pytest --cov=./ --cov-report=xml
