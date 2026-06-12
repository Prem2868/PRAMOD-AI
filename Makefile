# PRAMOD AI Automation Makefile
# Author: Pramod Jogdand | github.com/Prem2868
# © 2026 Pramod Jogdand. All rights reserved.

.PHONY: install run test clean

install:
	pip install -r requirements.txt

run:
	python main.py

test:
	python -m pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
