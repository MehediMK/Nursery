<h1 align='center'>Nursery Online Shop Using Django Framework</h1>


## Prerequisites
  - Python 3.8+
  - Postgres(if you want to ignore default sqlite database)
  - Virtualenv

## How to Run this Project

  - First of all clone this Project
  - Now go to the project directory
  - create a virtual env `virtualenv env`
  - Activate virtualenv `source env/bin/activate` (*linux) on `env\Scripts\activate` (Windows)
  - Install packages `pip install -r requirements.txt`
  - To configure your Postgres database and secret_key change file name from `config.py sample` to `config.py` change connections accordingly. 
    which is given project directory.
  - Run on terminal `python manage.py migrate`
  - Run `python manage.py runserver`

## Helpful commands
  - `python manage.py makemigrations` "for migration"
  - `python manage.py runserver host:port` "for starting dev. server"
  - `python manage.py startapp app_name` "for new app"
  - `python manage.py createsuperuser` "for create superuser"

****Note****: You can change phone number from footer and cart template



