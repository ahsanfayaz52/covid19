from __init__ import db

class japanCases(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    date = db.Column("date", db.String(100))
    pcr = db.Column("pcr", db.String(100))
    positive = db.Column("positive", db.String(100))
    symptom = db.Column("symptom", db.String(100))
    symptomless = db.Column("symptomless", db.String(100))
    symptomConfirming = db.Column("symptomConfirming", db.String(100))
    hospitalize = db.Column("hospitalize", db.String(100))
    mild = db.Column("mild", db.String(100))
    severe = db.Column("severe", db.String(100))
    confirming = db.Column("confirming", db.String(100))
    waiting = db.Column("waiting", db.String(100))
    discharge = db.Column("discharge", db.String(100))
    death = db.Column("death", db.String(100))

    def __init__(self, date, pcr, positive, symptom, symptomless,
                 symptomConfirming, hospitalize, mild,severe, confirming, waiting,discharge,death):
        self.date = date
        self.pcr = pcr
        self.positive = positive
        self.symptom = symptom
        self.symptomless = symptomless
        self.symptomConfirming = symptomConfirming
        self.hospitalize = hospitalize
        self.mild = mild
        self.severe = severe
        self.confirming = confirming
        self.waiting = waiting
        self.discharge = discharge
        self.death = death





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

class indiaCases(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    confirmed = db.Column("confirmed", db.String(100))
    deaths = db.Column("deaths", db.String(100))
    recovered = db.Column("recovered", db.String(100))

    def __init__(self, confirmed,deaths , recovered):
        self.deaths = deaths
        self.recovered = recovered
        self.confirmed = confirmed
