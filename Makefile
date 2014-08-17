run:
	./run.sh

setup:
	virtualenv ve
	(source ve/bin/activate && pip install -r requirements.txt)

test:
	(cd tests/ && python tests.py)
