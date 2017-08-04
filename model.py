
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db

class Companies(db.Model):
    companyId = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(80), nullable=False)
    industryField = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    def __init__(self,companyId, companyName, industryField, country):
        self.companyId = companyId
        self.companyName = companyName
        self.industryField = industryField
        self.country = country
    def __repr__(self):
        return '<Companies %r>' % self.companyName
    def as_dict(self):
        return {'companyId' : self.companyId, 'companyName' : self.companyName, 'industryField' : self.industryField, 'country' : self.country}
    def as_tuple(self):    
        company, stock = db.session.query(Companies, Stocks
                                                 ).filter(Stocks.companyId == self.companyId).first()
                      
        return (company.companyName, stock.ticker, company.industryField)

class Stocks(db.Model):
    ticker = db.Column(db.String(80))
    id = db.Column(db.Integer, primary_key=True)
    companyId = db.Column(db.Integer, db.ForeignKey(Companies.companyId))
    def __init__(self,ticker, id, companyId):
        self.ticker = ticker
        self.id = id
        self.companyId = companyId
    def __repr__(self):
        return '<Stocks %r>' % self.ticker
    def as_dict(self):
        company, stock = db.session.query(Companies, Stocks
                                                 ).filter(self.companyId == Companies.companyId).first()

        return {'companyName' : company.companyName, 'ticker' : self.ticker, 'industryField' : company.industryField}
    def as_tuple(self):
        company, stock = db.session.query(Companies, Stocks
                                                 ).filter(self.companyId == Companies.companyId).first()
        return (company.companyName, self.ticker, company.industryField)

class Stockvalues(db.Model):
    valueDate = db.Column(db.DateTime)
    stockId = db.Column(db.Integer, db.ForeignKey(Stocks.id))
    open = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float)
    volume = db.Column(db.Integer, nullable=False)
    valueId = db.Column(db.Integer, primary_key=True)
    def __init__(self, valueDate, stockId, open, close, volume, valueId):
        self.valueDate = valueDate
        self.stockId = stockId
        self.open = open
        self.close = close
        self.volume = volume
        self.valueId = valueId   
    def as_dict(self):
        value = db.session.query(Stockvalues).first()
        return {'valueDate' : value.valueDate, 'stockId' : value.stockId, 'open' : value.open, 'close' : value.close,'volume' : value.volume, 'valueId' : value.valueId}
    def as_tuple(self):
        value = db.session.query(Stockvalues).first()
        return (value.valueDate, value.stockId, value.open, value.close, value.volume, value.valueId)

    def __repr__(self):
        return '<Stockvalues %r>' % self.stockId
