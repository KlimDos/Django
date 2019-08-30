# Django

# Run:
```
VIRTUALENV=$(pwd)/Django

python3.7 -m venv $VIRTUALENV
source $VIRTUALENV/bin/activate
pip install Django 
django-admin startproject django.klimdos.ml
python3.7 manage.py startapp myapp
python3.7 manage.py migrate 
deactivate
```