# drf-bday-wisher

################################

# PREREQUISITE:
Make sure Redis is running on your localhost and port 6379. If redis is reachable in `127.0.0.1:6379` then we dont need to change the value of this variable `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` in `proj/settings.py`
I'm using sqlite as backend DB here. so no need for any external DB connection

# STEPS:
1. create virtual env using
    `python3 -m venv django_env`
2. activate the virtual env
    `source django_env/bin/activate`
3. install packages
    `pip install -r requirements.txt`
4. now cd to project directory
    `cd proj`
5. run migration
    ```
    `python3 manage.py makemigration`
    `python3 manage.py migrate`
    `python3 manage.py migrate django_celery_beat`
    ```
6. we need to open three terminal. one to run the api server, one to run celery worker and another to run celery beat
7. in the first terminal; run 
    ```
    `source django_env/bin/activate`
    `cd proj`
    `python3 manage.py runserver`
    ```
8. curl to post data
    ```
    curl --location 'http://127.0.0.1:8000/customers/api' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "My Name",
        "email": "email@mail.com",
        "bday": "2000-04-29"
    }'
    ```
9. curl to get data
    ``` 
    curl --location 'http://127.0.0.1:8000/customers/api'
    ```
10. then in the second terminal; run 
    ```
    source django_env/bin/activate
    cd proj
    celery -A bday_reminder worker -l INFO
    ```
11. then in the last terminal; run 
    ```
    source django_env/bin/activate
    cd proj
    celery -A bday_reminder beat -l INFO
    ```
job will be triggered on every 60 minutes. If any customers' birthday is on that day, it'll print a wish message in the console (this message will be displayed in the 2nd terminal where we ran the worker) and once this birthday message is displayed, it'll mark that customer is notified so that in next run it'll not send / display that message for the same customer.
another job will be troggerd in every 2 hours which will check if there was any customers' birthday day was in the previous day and its nofied flag is true. then it'll mark the notified tag to false.
