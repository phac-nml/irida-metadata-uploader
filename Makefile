SHELL=/bin/bash

requirements: clean env
	source .virtualenv/bin/activate
	pip3 install -e .

clean:
	rm -rf .virtualenv
	rm -rf build
	rm -rf dist
	find -name "*pyc" -delete

env:
	python3 -m venv .virtualenv
	source .virtualenv/bin/activate
	pip3 install --upgrade wheel pip
