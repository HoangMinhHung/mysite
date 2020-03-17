python manage.py runserver 0.0.0.0:$PORT
python manage.py collectstatic --noinput
web: gunicorn locallibrary.wsgi --log-file -
