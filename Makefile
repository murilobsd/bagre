MOD := bagre

lint:
	pylint $(MOD)
pep8:
	pycodestyle $(MOD)
clean:
	find . -not -path ".venv" -name "__pycache__" -type d -exec rm -rf {} \; || true
	find . -not -path ".venv" -name "*.pyc" -type f -exec rm -rf {} \; || true
