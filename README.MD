## General Overview

The applications stack is react using Next.js and MaterialUI, python using FastApi and Celery, PostgreSQL for the database and redis (required by Celery)

The whole application has been containerized and divided into different services that can interact with each other using docker compose. 

The way it works is the frontend makes request to the api in order to retrieve the logs or create messages. The messages are then polled every 6 seconds by a Celery worker and processed one by one in order to send the different types of notifications to every user that matches the criteria of the message.

## Before starting the application

You need to have docker and docker compose installed

Docker
https://docs.docker.com/desktop/

Docker Compose
https://docs.docker.com/compose/install/


## Initialize containers

After installing the required tools you just have to run the following commands

```bash
docker-compose build
docker-compose up 
```

if you dont want to see the ouput you can just run 
```bash
docker-compose up -d
```
## Users

By default the application initializes with 3 users, if you want to add more you can use the following route and payload (inside the body of the request) to add more
```bash
POST http://127.0.0.1:8000/users
{
    "name": "Mar",
    "email": "mar@test.com",
    "phone_number": "988266356",
    "subscribed": ["Sports"],
    "channels": ["email"]
}
```

or use the swagger in this URL
```bash
http://localhost:8000/docs#/
```

## Unit tests

In order to run the python tests youll need to enter the container with this command
```bash
docker-compose exec api bash
```
and once inside the container just run
```bash
pytest
```

