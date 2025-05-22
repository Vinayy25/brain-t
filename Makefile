.PHONY: setup train test run clean docker-build docker-run

# Development setup
setup:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Train the model
train:
	python mainTrain.py

# Test the model
test:
	python mainTest.py

# Run the web app
run:
	python app.py

# Clean up Python cache files
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type f -name '*.pyd' -delete
	find . -type f -name '.DS_Store' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} +
	find . -type d -name '*.egg' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

# Docker commands
docker-build:
	docker build -t brain-tumor-detection .

docker-run:
	docker run -p 5000:5000 brain-tumor-detection

# Help command
help:
	@echo "Available commands:"
	@echo "  make setup         - Install required dependencies"
	@echo "  make train         - Train the model"
	@echo "  make test          - Test the model"
	@echo "  make run           - Run the web application"
	@echo "  make clean         - Clean up Python cache files"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run Docker container" 