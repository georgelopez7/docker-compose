# Docker Compose: Flask App & mySQL Database

![Blank diagram (2)](https://user-images.githubusercontent.com/71076769/220912650-abd99f7b-6e84-46bd-91e4-5fbd2c979bbb.svg)


---

### Table of Contents

- [Description](#description)
- [Flask Application](#flask-application)
- [Folder Hierarchy](#folder-hierarchy)
- [docker-compose file](#docker-compose-file)
- [Author Info](#author-info)

---

## Description

In this repository, you will see how I created a Flask application using Python and connected it to a MySQL database, with each component running in a separate container in Docker. This project takes advantage of Docker Compose which is used to create multi-container systems using a **docker-compose.yml** file which can be read about further in this document.

[Back To The Top](#docker-compose-flask-app--mysql-database)

---

## Flask Application

This Flask application is a simple to-do list that allows users to input and remove tasks, with each task being stored and saved in a MySQL database. The code for the flask application can be found **python/flask_app.py**

Below is a video of the application in use:


https://user-images.githubusercontent.com/71076769/220915783-4800be0c-a901-4b3b-b99d-9592a8dc7791.mp4



[Back To The Top](#docker-compose-flask-app--mysql-database)

---

## Folder Hierarchy

Below you can see an image of the folder hierachy required to produce this containerized infrastructure for this project:

![Screenshot 2023-02-22 123123](https://user-images.githubusercontent.com/71076769/220620673-c797ab89-5418-4a58-a29e-caf2a5828967.png)

[Back To The Top](#docker-compose-flask-app--mysql-database)

---

## docker-compose file

Below is an explanation of the docker-compose.yml file that was used to compose this project:

![Screenshot 2023-02-22 123213](https://user-images.githubusercontent.com/71076769/220620646-b623cfdd-857e-43ff-ae0d-c9bb4df44160.png)

[Back To The Top](#docker-compose-flask-app--mysql-database)

---


## Author Info

LinkedIn - [George Lopez](https://www.linkedin.com/in/george-benjamin-lopez/)

[Back To The Top](#docker-compose-flask-app--mysql-database)
