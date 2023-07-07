python -m venv env
.\env\Scripts\Activate.ps1
pip install django gunicorn whitenoise
django-admin startproject tourist
python -m pip freeze > requirements.txt
cd tourist

python manage.py startapp touristapp
python manage.py migrate
python manage.py runserver Localhost:8001
cd touristapp

docker compose up --build

pip install django-environ

