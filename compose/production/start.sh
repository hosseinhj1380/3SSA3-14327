#!/bin/bash

echo migration 

python manage.py collectstatic --noinput

python manage.py migrate

echo "Run Gunicorn Server"

  exec gunicorn -c ./gunicorn.py.ini config.wsgi
# fi