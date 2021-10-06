deps:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	isort backend
	flake8 backend

test:
	cd backend && pytest
	rm -r backend/media/recipes

coverage:
	cd backend && pytest --cov=./ --cov-report=xml
