from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///theVirusTracker.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///covidApi.sqlite3'


db =  SQLAlchemy(app)




class theVirusTracker(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    total_cases = db.Column("total_cases", db.String(100))
    total_recovered = db.Column("total_recovered", db.String(100))
    total_unresolved = db.Column("total_unresolved", db.String(100))
    total_deaths = db.Column("total_deaths", db.String(100))
    total_new_cases_today = db.Column("total_new_cases_today", db.String(100))
    total_new_deaths_today = db.Column("total_new_deaths_today", db.String(100))
    total_active_cases = db.Column("total_active_cases", db.String(100))
    total_serious_cases = db.Column("total_serious_cases", db.String(100))
    total_affected_countries = db.Column("total_affected_countries", db.String(100))
    source = db.Column("source", db.String(100))

    def __init__(self, total_cases, total_recovered, total_unresolved, total_deaths, total_new_cases_today,
                 total_new_deaths_today, total_active_cases, total_serious_cases, total_affected_countries, source):
        self.total_cases = total_cases
        self.total_recovered = total_recovered
        self.total_unresolved = total_unresolved
        self.total_deaths = total_deaths
        self.total_new_cases_today = total_new_cases_today
        self.total_new_deaths_today = total_new_deaths_today
        self.total_active_cases = total_active_cases
        self.total_serious_cases = total_serious_cases
        self.total_affected_countries = total_affected_countries
        self.source = source





class covidApi(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    date = db.Column("date", db.String(100))
    last_update = db.Column("last_update", db.String(100))
    confirmed = db.Column("confirmed", db.String(100))
    confirmed_diff = db.Column("confirmed_diff", db.String(100))
    deaths = db.Column("deaths", db.String(100))
    deaths_diff = db.Column("deaths_diff", db.String(100))
    recovered = db.Column("recovered", db.String(100))
    recovered_diff = db.Column("recovered_diff", db.String(100))
    active = db.Column("active", db.String(100))
    active_diff = db.Column("active_diff", db.String(100))
    fatality_rate = db.Column("fatality_rate", db.String(100))
    def __init__(self, date , last_update , confirmed,
                 confirmed_diff, deaths, deaths_diff, recovered, recovered_diff,active,active_diff,fatality_rate):
        self.date = date
        self.last_update = last_update
        self.confirmed = confirmed

        self.confirmed_diff = confirmed_diff
        self.deaths = deaths
        self.deaths_diff = deaths_diff
        self.recovered = recovered
        self.recovered_diff = recovered_diff
        self.active = active
        self.active_diff = active_diff
        self.fatality_rate = fatality_rate