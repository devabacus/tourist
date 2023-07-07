# python.exe -m pip install --upgrade pip
python -m venv env
.\env\Scripts\Activate.ps1
pip install django
pip install djangorestframework
django-admin startproject telegram_bot
cd .\telegram_bot
python manage.py startapp bot_app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser