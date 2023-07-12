# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim

EXPOSE 8001

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./tourist /app

# Collect static files
RUN python manage.py collectstatic --no-input

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "tourist.wsgi"]
# CMD [ "python", "manage.py","runserver", "0.0.0.0:8001" ]
# CMD ["gunicorn", "--bind", "0.0.0.0:8350", "--reload", "touristhelper.wsgi:application"]
