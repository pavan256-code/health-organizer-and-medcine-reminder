.PHONY: help install run dev build test lint clean migrate seed docker-build docker-up

PYTHON ?= python
PIP ?= pip
MANAGE ?= $(PYTHON) manage.py

help:
	@echo "Available commands:"
	@echo "  make install      Install production and development dependencies"
	@echo "  make run          Start development server on port 8000"
	@echo "  make migrate      Apply database schema migrations"
	@echo "  make seed         Seed clinical demo records and medicines"
	@echo "  make test         Execute complete test suite"
	@echo "  make coverage     Generate test coverage report"
	@echo "  make build        Collect static files and validate assets"
	@echo "  make lint         Run code style and syntax checks"
	@echo "  make clean        Remove cache, build artifacts and temporary files"
	@echo "  make docker-build Build multi-stage Docker container"
	@echo "  make docker-up    Run application stack with Docker Compose"

install:
	$(PIP) install -r requirements.txt

run dev:
	$(MANAGE) runserver 0.0.0.0:8000

migrate:
	$(MANAGE) migrate

seed:
	$(MANAGE) seed_demo_data
	$(MANAGE) seed_more_medicines

test:
	$(PYTHON) -m pytest

coverage:
	$(PYTHON) -m pytest --cov=apps --cov=config --cov-report=html --cov-report=term

build:
	$(MANAGE) collectstatic --noinput

lint:
	flake8 apps config --max-line-length=120 --exclude=*/migrations/*

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .coverage htmlcov .pytest_cache dist build 2>/dev/null || true

docker-build:
	docker build -t health-organizer:latest .

docker-up:
	docker compose up -d
