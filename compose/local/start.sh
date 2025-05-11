#!/bin/bash

echo migration 

python manage.py makemigrations 
python manage.py migrate

echo "Run  Server"

  python manage.py runserver 0.0.0.0:8000 
  
# fi