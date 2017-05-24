
from flask_testing import TestCase
from flask import Flask
import flask
import mock
from app import app, db
from model import Companies, Stocks, Stockvalues
import json

def create_db_and_data():
    db.create_all()

class StocksTestCase(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.secret_key = 'some_secret'
        SQLALCHEMY_DATABASE_URI = 'sqlite://'        
        return app

    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass    
        
    def test_access_noredirect(self):
        rv = self.test_app.get('/')
        self.assertEqual(rv.status_code,200)

    def test_correct_format(self):
        rv = self.test_app.post('/showShares/', data=dict(
            alkupvm='2015-11-5',
            loppupvm='2015-11-9'))
        self.assertEqual(rv.status_code,200)
        return rv   

    def test_incorrect_format(self):
        rv = self.test_app.post('/showShares/', data=dict(
            alkupvm='2015-99-5',
            loppupvm='2015-11-9'))
        print "rv.data ",rv.data
        self.assertEqual(rv.status_code,0)
        self.assertIn('month must be in 1..12', rv.data)
        return rv


if __name__ == '__main__':
    import nose
    nose.main(defaultTest=__name__)
