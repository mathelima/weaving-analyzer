PYTHON=python3
VENV=.venv
ACTIVATE=. $(VENV)/bin/activate

.PHONY: install run server test lint clean

# Create virtual environment and install dependencies
install:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) && pip install --upgrade pip
	$(ACTIVATE) && pip install -r requirements.txt

# Run the main application
run:
	$(ACTIVATE) && python main.py

# Run the local server used for testing
server:
	$(ACTIVATE) && python server/server.py

# Run unit tests
test:
	$(ACTIVATE) && pytest -v

# Run static analysis
format:
	$(ACTIVATE) && isort . && black .

# Run static analysis
lint:
	$(ACTIVATE) && flake8 src tests

# Clean caches and temporary files
clean:
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf .pytest_cache
	rm -rf $(VENV)
