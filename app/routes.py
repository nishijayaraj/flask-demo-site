from itertools import islice
from flask import render_template
from app import app
import requests


@app.route('/')
@app.route('/index')
def index():
  title = "sample app"
  url = "http://localhost:9000"
  #res = requests.get(url)
  #data=res.json()
  data = [ {
    "Timestamp": 0,
    "Voltage": 0,
    "Current": 0,
    "Resistance": 0}]
    
  return render_template("index.html",title=title, data=data[0]) 
