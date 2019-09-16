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

```
install docker docker-compose
git clone
cd compose/
docker compose up
sudo docker-compose run web ./manage.py migrate


```
https://www.youtube.com/watch?v=iKB_4HWKMCc
mongodb+srv://sasha:<password>@cluster0-srkrs.gcp.mongodb.net/test?retryWrites=true&w=majority