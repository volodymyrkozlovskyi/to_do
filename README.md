## This is a second part of DevOps interview test

### Terraform infrastructure code and description located here - https://github.com/volodymyrkozlovskyi/interview_infrastructure


In this repo you will find a simple To Do application written in Python/Django with MySql database and NGINX proxy.
To run this app you will need to install docker and docker-compose.

  ```sudo docker-compose -f docker-compose-deploy.yml up --build -d ```


After all containers up and running you will need to run
  ```sudo docker-compose -f docker-compose-deploy.yml run app python manage.py migrate```
to migrate database schema
