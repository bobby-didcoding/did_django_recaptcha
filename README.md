# did_django_recaptcha
Django project that users the reCAPTCHA API

1) cd to development directory
2) mkvirtualenv did_django_recaptcha
3) mkdir did_django_recaptcha
4) clone repository to new directory
5) pip install -r requirements.txt
6) Update settings.py with your email API information

if DEBUG:
    RECAPTCHA_PUBLIC_KEY = 'XXX'
    RECAPTCHA_PRIVATE_KEY = 'XXX'
else:
    RECAPTCHA_PUBLIC_KEY = 'XXX'
    RECAPTCHA_PRIVATE_KEY = 'XXX'


7) python manage.py makemigrations
8) python manage.py migrate
9) python manage.py runserver
10) https://localhost:8000 - Bob's your uncle!! 

