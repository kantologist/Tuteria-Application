This is my submission for the Tuteria Application. Thanks

# create virtual environment by running
$ virtualenv env

# activate it with
$ source env/scripts/activate  # for windows
$ source env/bin/activate  # for linux os

# install requirements from txt with
$ pip install -r requirements.txt

# install postgre database and set password for the default user postgres. 
# create database Guinness, which is the project name. 
# or change Guinness/settings.py to use sqlite3 

# to migrate database. run
$ python manage.py syncdb

# migrate app with south
$ python manage.py schemamigrations guinnessnigeria
$ python manage.py migrate guinnessnigeria

$ python manage.py migrate


# to test app 
$ python manage.py runserver 0.0.0.0:8000

go to http://localhost:8000