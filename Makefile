.PHONY: test

ROOT_DIR = ${CURDIR}
export FLASK_APP=controller/main.py
export FLASK_ENV=development

test:
	env PYTHONPATH=$(ROOT_DIR) pytest

run-container: run-container

run-server:
	flask run
