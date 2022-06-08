install: 
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
test:
	python -m pytest -vv test_main.py
	
format:
	black *.py
	

lint:
	pylint --disable=R,C,W0702 main.py
	
all: install lint test