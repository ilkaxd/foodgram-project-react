deps:
	python -m pip install --upgrade pip
	pip install --upgrade pip
	pip install -r requirements.txt
fix:
	isort backend
	flake8 backend
test:
	cd backend
	flake8
	pytest
