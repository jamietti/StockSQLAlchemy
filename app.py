from flask import Flask, render_template, request, json, flash
from model import db, app, Companies, Stocks, Stockvalues 
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import operator

#app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = 'some_secret'
Session(app)

class ValidationError(Exception):
    pass

@app.route("/",methods=['POST', 'GET'])
def main():
  data = list()  
  for stock in db.session.query(Stocks):
    data.append(stock.as_tuple())
  return render_template('stocks.html',data=data)
   
@app.route('/showShares/',methods=['POST'])
def showShares():
  alku=request.form['alkupvm']
  loppu=request.form['loppupvm']
 
  kasvut={}
  try:
    for stock_id in db.session.query(Stocks):
      eka = db.session.query(Stockvalues).filter(Stockvalues.stockId==stock_id.id,Stockvalues.valueDate >= pd.to_datetime(alku)).order_by(Stockvalues.valueDate).first()
      alkuarvo=eka.close
      pienin=eka.valueDate
      for apu in db.session.query(Stockvalues).filter(Stockvalues.stockId==stock_id.id,Stockvalues.valueDate <= pd.to_datetime(loppu)).order_by(Stockvalues.valueDate):
        pass
      suurin=apu.valueDate
      loppuarvo=apu.close
      kasvut[ stock_id.id ] = ( loppuarvo - alkuarvo )/alkuarvo * 100    
    sorted_kasvut=sorted(kasvut.items(),key=lambda x: (-x[1], x[0]))
  except Exception as e:
    return (e.args[0], "error")
  data = list()     
  for kasvu in sorted_kasvut:
    stock=db.session.query(Stocks).filter(Stocks.id==list(kasvu)[0]).first()
    company=db.session.query(Companies).filter(Companies.companyId==stock.id).first()   
    data.append((company.companyName, company.industryField, list(kasvu)[1]))
  return render_template('kasvut.html',alku=alku, loppu=loppu, data=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
