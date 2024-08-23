.PHONY: install virtualenv 

install:
	@echo "installing for dev invironment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv./bin/python -pip -m venv .venv



