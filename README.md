# **Table of Contents**
  
 * [Modules](#modules)
 * [Usage](#usage)
 * [Description](#description)
 * [DataBase](#database)


# Modules

- Restaurant manager.
- Node.js Frontend.
- Django Backend.
- PnP module (Plug-and-Play).

# Description
>Project of higher degree of multiplatform application development. 

>We propose the simulation of a company that has contracted a freelance programmer to implement its website. 

>This company needs to manage its chain of restaurants and everything that goes with it.

>Only customers, staff, reservations and restaurant departments will enter this web application.

# Usage
- DataBase Steps (PSQL)
   - Create database

      ```bash
        CREATE DATABASE name-of-database;
      ```
      
   - Create user

      ```bash
        CREATE USER name-of-user;
      ```
      
   - Set password to user

      ```bash
        ALTER USER name-of-user WITH PASSWORD 'password';
      ```
      
   - Grant privileges to database

      ```bash
        GRANT ALL PRIVILEGES ON DATABASE name-of-database TO name-of-user;
      ```
      
   - Enter database and create extensions

      ```bash
        \c name-of-database
        CREATE EXTENSION IF NOT EXISTS unaccent;
        CREATE EXTENSION IF NOT EXISTS pg_trgm;
      ```

- Backend Steps
   - Recommended python 3.10
   - Configure the core/settings/local.py file with your database data
   - Create a virtual environment

      ```bash
        python -m venv envback
      ```

   - Turn on the virtual environment

      ```bash
        envback\Scripts\activate.bat
      ```
    
    - Install requirements
    
      ```bash
        pip install -r requirements.txt
      ```
      
   - Create the migrations

      ```bash
        python manage.py makemigrations
      ```
      
   - Apply the migrations to data base

      ```bash
        python manage.py migrate
      ```
      
   - Create a superuser

      ```bash
        python manage.py createsuperuser
      ```
      
   - Run these codes to have some pre-defined data

      ```bash
        python manage.py 1_location
        python manage.py 2_user
        python manage.py 3_profile
        python manage.py 4_restaurant
        python manage.py 5_lead
      ```
      
   - Start Server on http://localhost:8000/admin/

       ```bash
        python manage.py runserver
      ```

- Frontend Steps
   - Recommended node 16.20 LTS
   - Install Yarn with NPM
   
      ```bash
        npm install yarn
      ```
      
   - Install modules to run proyect

      ```bash
        yarn install
      ```
      
   - Start server on http://localhost:3000

      ```bash
        yarn doit
      ```
      
# DataBase
![](https://github.com/josesanfri/ProyectoJSF/blob/main/TFGProjectJSF.drawio.png)
