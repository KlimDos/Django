# Django

# Run:
```
VIRTUALENV=$(pwd)/venv

python3.7 -m venv $VIRTUALENV
===
python3.7 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt #or pip install Django
django-admin startproject mysite
python3.7 manage.py startapp myapp
python3.7 manage.py migrate 
deactivate
```