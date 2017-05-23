# StockSQLAlchemy
## Task to do

Task is to implement a web application to list all stocks from given SQLite database and calculate and show on web page the company/stock specific share price growths in user defind period.


# The solution

## Used technologies

PYTHON, FLASK, SQLALCHEMY, CSS, HTML, SQLite.
And of course python virtualenv.

## Create the environment in ubuntu

    sudo apt-get install virtualenv
    sudo apt-get install python-pip python-dev build-essential
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

## Run the service

Before you run the service you have to create a virtual environment.
In StockSQLAlchemy directory give commands

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

And run the service

    python app.py

The service is now running at localhost:5000

