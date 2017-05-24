# StockSQLAlchemy/test
## 

This directory includes some examples of python unit tests



## Run the test

Before you run the service you have create a virtual environment.
In StockSQLAlchemy directory give commands

    virtualenv venv
    source venv/bin/activate

Go to test directory

    cd test
    pip install -r requirements.txt

Define environment variable PYTHONPATH

    export PYTHONPATH=..:$PYTHONPATH

And run the test cases 

    nosetests --nocapture test_stocks.py    

