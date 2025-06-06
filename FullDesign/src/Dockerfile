FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collecte les fichiers statiques
RUN python manage.py collectstatic --noinput

# Lancer gunicorn en production
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
