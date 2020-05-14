from flask import Flask,request,render_template,redirect,url_for
from flask_restful import Resource, Api
import requests
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__ )
import json

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib3

app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thevirustracker.sqlite3'



db =  SQLAlchemy(app)


class theVirusTracker(db.Model):
     id = db.Column("id",db.Integer,primary_key=True)
     total_cases = db.Column("total_cases",db.String(100))
     total_recovered = db.Column("total_recovered",db.String(100))
     total_unresolved = db.Column("total_unresolved",db.String(100))
     total_deaths = db.Column("total_deaths",db.String(100))
     total_new_cases_today = db.Column("total_new_cases_today",db.String(100))
     total_new_deaths_today = db.Column("total_new_deaths_today",db.String(100))
     total_active_cases = db.Column("total_active_cases",db.String(100))
     total_serious_cases = db.Column("total_serious_cases",db.String(100))
     total_affected_countries = db.Column("total_affected_countries",db.String(100))
     source = db.Column("source",db.String(100))
     def __init__(self,total_cases,total_recovered,total_unresolved,total_deaths,total_new_cases_today,total_new_deaths_today,total_active_cases,total_serious_cases,total_affected_countries,source):
         self.total_cases = total_cases
         self.total_recovered = total_recovered
         self.total_unresolved = total_unresolved
         self.total_new_cases_today = total_new_cases_today
         self.total_new_deaths_today = total_new_deaths_today
         self.total_active_cases = total_active_cases
         self.total_serious_cases = total_serious_cases
         self.total_affected_countries = total_affected_countries
         self.source = source


@app.route('/virusTracker',methods=["POST","GET"])
def index():
    if request.method=="GET":
        total_cases = 0
        url =  "https://api.thevirustracker.com/free-api?global=stats"
        """ 
        req = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        page_soup = BeautifulSoup(webpage,"html.parser")
        total_cases = page_soup.findAll("pre" )
        print(total_cases)
        return total_cases
    """
        html_content =  requests.get(url).text
        soup = BeautifulSoup(html_content,"lxml")
        data = soup.find("p").text
        return data















if __name__ == '__main__':
    db.create_all()
    app.run( debug=True   )


