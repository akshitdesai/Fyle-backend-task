# Fyle-backend-task

To set django server in local:-

Install pipenv:
```
pip install pipenv
```

export environment variable for db and secret key of django project:-
```
export DATABASE_HOST = <HOST_URL>
export DATABASE_NAME = <DATABASE_NAME>
export DATABASE_PASSWORD = <DATABASE_PASSWORD>
export DATABASE_URL = <DATABASE_URL>
export DATABASE_USER = <DATABASE_USER>

export SECRET_KEY = <SECRET_KEY>
```

After cloning repo:-
```
# install all dependancy
pipenv install

# activate virtual environment
pipenv shell

# change directory to django project
cd fylebanks

# migrate models
python manage.py migrate

# to runserver
python manage.py runserver
```

To load data from csv file:-
```
python manage.py load_data data.csv
```
