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
      - Command: CREATE DATABASE name-of-database;
   - Create user
      - Command: CREATE USER name-of-user;
   - Set password to user
      - Command: ALTER USER name-of-user WITH PASSWORD 'password';
   - Grant privileges to database
      - Command: GRANT ALL PRIVILEGES ON DATABASE name-of-database TO name-of-user;
   - Enter database and create extensions
      - Command: \c name-of-database
      - Command: CREATE EXTENSION IF NOT EXISTS unaccent;
      - Command: CREATE EXTENSION IF NOT EXISTS pg_trgm;

- Backend Steps
   - Recommended python 3.10
   - Turn on the virtual environment
      - Command: envback\Scripts\activate.bat
   - Create the migrations
      - Command: python manage.py makemigrations
   - Apply the migrations to data base
      - Command: python manage.py migrate
   - Start Server
      - Command: python manage.py runserver

- Frontend Steps
   - Recommended node 16.20 LTS
   - Install Yarn with NPM
      - Command: npm install yarn
   - Install modules to run proyect
      - Command: yarn install
   - Start server
      - Command: yarn doit
      
# DataBase
![](https://github.com/josesanfri/ProyectoJSF/blob/main/TFGProjectJSF.drawio.png)
