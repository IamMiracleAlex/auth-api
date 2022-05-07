# Live URL
`https://zuri-auth-api.herokuapp.com/docs/`


# Functionalities
1. signup user 
2. login user
4. list all users
5. refresh token
6. verify token


# Development
1.  clone the repository
2.  create a virtual environment running python 3.8 (or above) - and activate it
    `python3 -m venv env` to create, and `source env/bin/activate` to activate (mac and linux) or `source env/Scripts/activate` (windows with `bash`)
3.  cd into the root of the django project (i.e the path containing manage.py)
4.  install requirements `pip install -r requirements.txt`
5.  run `python manage.py migrate` to create database tables
6.  run `python manage.py createsuperuser` to create a superuser(An initial user that has access to the admin site)
7. run `python manage.py runserver` to start the development server

The application should now be running on port 8000, `localhost:8000`
