
from flask_testing import TestCase
from flask import Flask
import flask
import mock
from app import app, db
from sqlalchemy import *
from model import Companies, Stocks, Stockvalues
import datetime


class StocksTestCase(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.secret_key = 'some_secret'
        SQLALCHEMY_DATABASE_URI = 'sqlite://'        
        db.drop_all()
        db.create_all()
        new_cmp = Companies(1,
                          "testCompany",
                          "testing",
                          "Finland")
        db.session.add(new_cmp)
        new_stock = Stocks("TST",
                          1,
                          1)

        db.session.add(new_stock)

        new_stock_value = Stockvalues(datetime.datetime(2015, 5, 24),
                          1,  
	                  111,
                          0,
                          777,
                          1)
        db.session.add(new_stock_value)
   
        new_stock_value = Stockvalues(datetime.datetime(2015, 6, 24),
                          1,
                          1111,
                          1222,
                          777,
                          2)
        db.session.add(new_stock_value)

        new_stock_value = Stockvalues(datetime.datetime(2017, 5, 24 ),
                          1,
                          1111,
                          1223,
                          777,
                          3)
        db.session.add(new_stock_value)

        db.session.commit()  
        return app

    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass    
        
    def test_task1(self):
        rv = self.test_app.get('/')
        self.assertEqual(rv.status_code,200)
        self.assertIn('testCompany', rv.data)
        self.assertIn('TST', rv.data)
        self.assertIn('testing', rv.data) 
        return rv

    def test_correct_format_no_data(self):
        rv = self.test_app.post('/showShares/', data=dict(
            alkupvm='2014-11-5',
            loppupvm='2014-11-9'))
        self.assertEqual(rv.status_code,200)
        self.assertIn('N/A', rv.data)
        return rv   

    def test_correct_format_data_found(self):
        rv = self.test_app.post('/showShares/', data=dict(
            alkupvm='2015-6-23',
            loppupvm='2017-5-25'))
        self.assertEqual(rv.status_code,200)
        self.assertNotIn('N/A', rv.data)
        return rv

    def test_incorrect_format(self):
        rv = self.test_app.post('/showShares/', data=dict(
            alkupvm='2015-99-5',
            loppupvm='2015-11-9'))
        self.assertEqual(rv.status_code,0)
        self.assertIn('month must be in 1..12', rv.data)
        return rv

if __name__ == '__main__':
    import nose
    nose.main(defaultTest=__name__)
