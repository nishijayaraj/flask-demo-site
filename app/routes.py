from itertools import islice
from flask import render_template
from app import app
import requests


@app.route('/')
@app.route('/index')
def index():
  title = "sample app"
  url = "http://www.mocky.io/v2/5a6485cf2b00000509f41487"
  res = requests.get(url)
  print('*************')
  print res
  data=res.json()
  print data
  display_items = ["Timestamp","Voltage","Current", "Resistance", "Battery", "Vehicle speed","Diagnostic message","Engine speed", "Engine oil level", "Coolant level"]
  '''data = [ {
    "Timestamp": 0,
    "Voltage": 0,
    "Current": 0,
    "Resistance": 0}]'''
    
  return render_template("index.html",title=title, data=data[0], display_items = display_items) 
