setup:
	python3 -m venv ~/.udacity-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test_app.py
	#python -m pytest --nbval notebook.ipynb


lint:
	pylint app.py

all: install lint test
