![Logo](neighborhoodApp/static/images/knoxlogofull.png)

# City of Knoxville Neighborhood Portal
  The Neighborhood Portal is an app that allows users from the Knoxville Office of Neighborhoods to manage and view data related to neighborhood organizations and their resident members. The public can also use the app to view basic information on neighborhood organizations.

## Table of Contents
  * [Features List](#features-list)
  * [Technologies Used](#technologies-used)
  * [Installing and Launching the App](#installing-and-running-the-app)
  * [Planning Documentation](#planning-documentation)
    * [Entity Relationship Diagram](#entity-relationship-diagram)

## Features List

### Feature
  feature description & image

### Feature
  feature description & image

### Feature
  feature description & image

### Feature
  feature description & image

### Feature
  feature description & image
  
  
### Feature
  feature description & image  

## Technologies Used
  ![Python](neighborhoodApp/static/images/icons8-python-48.png)
  ![Django](neighborhoodApp/static/images/icons8-django-48.png)
  ![HTML](neighborhoodApp/static/images/icons8-html-filetype-48.png)
  ![CSS](neighborhoodApp/static/images/icons8-css3-48.png)
  ![JavaScript](neighborhoodApp/static/images/icons8-javascript-48.png)
  ![SQLite](neighborhoodApp/static/images/icons8-sql-48.png)

## Installing and Running the App

  ----------------

  Clone this repo on your personal machine using the following command in your terminal
  ```sh
    git clone git@github.com:NSS-Post-Grad/knxhx-city-challenge.git
  ```

  Create and activate a virtual environment
  ```sh
    cd knxhx-city-challenge
    python manage.py venv cityDataEnv
    source ./cityDataEnv/bin/activate
  ```

  Install dependencies
  ```sh
    pip install requirements.txt
  ```

  Make migrations and migrate to create your database structure
  ```sh
    python manage.py makemigrations
    python manage.py migrate
  ```

  Load fixture data
  ```sh
    python manage.py loaddata neighborhood_org
    python manage.py loaddata resident
  ```
  
  Create a superuser, and follow the instructions in your terminal when prompted
  ```sh
    python manage.py createsuperuser
  ```

  To run the server, type
  ```sh
    python manage.py runserver
  ```

  Now that the server is up and running, you can open an internet browser and access the application
  ```sh
    http://localhost:8000/
  ```

## Planning Documentation

### Entity Relationship Diagram
![Neighborhood Portal ERD](neighborhoodApp/static/images/neighborhoodERD.png)

  