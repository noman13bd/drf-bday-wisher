# drf-bday-wisher

################################


PREREQUISITE:

    Make sure Redis is running on your localhost and post 6379. If redis is reachedable in `127.0.0.1:6379` then we dont need to change the value of this variable `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` in `proj/settings.py`

    I'm using sqlite here. so no need for any external DB connection

STEPS:

    1. create virtual env using
    ```python3 -m venv django_env```
    2. activate the virtual env
    ```source django_env/bin/activate```
    3. install packages
    ```pip install -r requirements.txt```
    4. now cd to project directory
    ```cd proj```
    5. run migration
    ```python3 manage.py makemigration```
    ```python3 manage.py migrate```
    6. we need to open three terminal. one to run the api server, one to run celery worker and another to run celery beat
    7. in the first terminal; run ```python3 manage.py runserver```
    8. curl to post data
    ```curl --location 'http://127.0.0.1:8000/customers/api' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "My Name4",
        "email": "noman@nom.com",
        "bday": "2000-04-29"
    }'```
    9. curl to get data
    ```curl --location 'http://127.0.0.1:8000/customers/api'```
    10. then in the second terminal; run ```celery -A bday_reminder worker -l INFO```
    11. then in the last terminal; run ```celery -A bday_reminder beat -l INFO```


