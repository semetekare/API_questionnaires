#!/bin/sh

python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py collectstatic --no-input --clear

gunicorn api.wsgi:application --bind 0.0.0.0:8000
