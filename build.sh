#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed data
python seed_data.py

# Collect static files
python manage.py collectstatic --noinput
