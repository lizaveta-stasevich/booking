web: ( cd src && gunicorn --workers 2 core.wsgi:application --bind 0.0.0.0:$PORT )
# web: python src/manage.py runserver 0.0.0.0:$PORT
release: python src/manage.py migrate
