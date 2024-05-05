# drf-bday-wisher

################################

# STEPS:
First clone project and then cd into the folder. Then follow the steps below:
1. build the container
    `docker compose build`
2. run the services
    `docker compose up` # provide `-d` if want to run in detached mode
3. curl to post data
    ```
    curl --location 'http://127.0.0.1:8000/customers/api' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "My Name",
        "email": "email@mail.com",
        "bday": "2000-04-29"
    }'
    ```
4. curl to get data
    ``` 
    curl --location 'http://127.0.0.1:8000/customers/api'
    
job will be triggered on every 2 hours. If any customers' birthday is on that day, it'll print a wish message in the console (this message will be displayed in the celery worker container) and once this birthday message is displayed, it'll mark that customer is notified so that in next run it'll not send / display that message for the same customer.
another job will be troggerd in every 2 hours which will check if there was any customers' birthday day was in the previous day and its nofied flag is true. then it'll mark the notified tag to false.
If we want to see the console logs we can get the container id and run this `docker logs -f [container_id]` command
