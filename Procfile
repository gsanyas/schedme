web: echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@schedme.com', 'admin')" | python app/manage.py shell && gunicorn app.wsgi --chdir ./app --log-file -