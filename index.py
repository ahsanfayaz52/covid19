from flask import Flask,request,render_template,redirect,url_for
from flask_restful import Resource, Api
import requests



import re
from bs4 import BeautifulSoup

from Models import theVirusTracker,covidApi,indiaCases
from Models import db,app




@app.route('/fetch',methods=["POST","GET"])
def index():

    if request.method=="GET":

        Apis = []
        url1 =  "https://api.thevirustracker.com/free-api?global=stats"
        url2 = "https://covid-api.com/api/reports/total?date=2020-04-15"
        url3 = "https://covid19-stats-api.herokuapp.com/api/v1/cases?country=India"

        Apis.append(url1)
        Apis.append(url2)
        Apis.append(url3)

        extractDataFromApis(Apis)






        return "added successfully"





def extractDataFromApis(urls):

    i = 1
    for url in urls:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        data = soup.find("p").text

        res = re.findall(r'\w+', data)
        values = re.split("[a-z]", str(res))

        numbers = re.findall(r'\d+', str(values))



        if i==1:


            addDataToVirusTracker(numbers,url)

        if i == 2:

            addDataToCovidApi(numbers)
        if i == 3:

            addDataToIndiaApi(numbers)

        i = i + 1











def addDataToVirusTracker(numbers,url):
    total_cases = numbers[0]
    total_recovered = numbers[1]
    total_unresolved = numbers[2]
    total_deaths = numbers[3]
    total_new_cases_today = numbers[4]
    total_new_deaths_today = numbers[5]
    total_active_cases = numbers[6]
    total_serious_cases = numbers[7]
    total_affected_countries = numbers[8]
    source = url


    data = theVirusTracker(total_cases,total_recovered,total_unresolved,total_deaths,total_new_cases_today,total_new_deaths_today,total_active_cases,total_serious_cases,total_affected_countries,source)

    db.session.add(data)
    db.session.commit()



def addDataToCovidApi(numbers):
    data = numbers[0] + "-" + numbers[1] + "-" + numbers[2]
    last_update = numbers[3] + "-" + numbers[4] + "-" + numbers[5] + " " + numbers[6] + ":" + numbers[7] + ":" + \
                  numbers[8]
    confirmed = numbers[9]
    confirmed_diff = numbers[10]
    deaths = numbers[11]
    deaths_diff = numbers[12]
    recovered = numbers[13]
    recovered_diff = numbers[14]
    active = numbers[15]
    active_diff = numbers[16]
    fatality_rate = numbers[17]

    covidApiData = covidApi(data, last_update, confirmed, confirmed_diff, deaths, deaths_diff, recovered,
                            recovered_diff, active, active_diff, fatality_rate)

    db.session.add(covidApiData)
    db.session.commit()


def addDataToIndiaApi(numbers):
    confirmed = numbers[0]
    deaths = numbers[1]
    recovered = numbers[2]
    print(numbers)


    indiaApiData =   indiaCases(confirmed,deaths,recovered)
    db.session.add(indiaApiData)
    db.session.commit()








@app.route('/delete/<data>',methods=["POST","GET"])
def deleteDataFromDatabase(data):

    if request.method == "GET":
        if data == "virusTracker":
            try:
                rows = db.session.query(theVirusTracker).delete()
                db.session.commit()

                show = rows + " removed successfully"
            except:
                db.session.rollback()
                show = "no rows available"
        elif data == "covidApi":
            try:
                rows = db.session.query(covidApi).delete()
                db.session.commit()

                show = rows + " removed successfully"
            except:
                db.session.rollback()
                show = "no rows available"
        elif data == "indiaCases":
            try:
                rows = db.session.query(indiaCases).delete()
                db.session.commit()

                show = rows + " removed successfully"
            except:
                db.session.rollback()
                show = "no rows available"
        else:
            print("sorry no route sexist")




        return "hello"

@app.route('/getData/<data>',methods=["POST","GET"])
def getDataFromDatabase(data):

    if request.method == "GET":
        if data == "virusTracker" :
            data = theVirusTracker.query.all()
            print("data = " + str(data))
            for item in data:
                print(item.total_cases)


        elif data == "covidApi":
            data = covidApi.query.all()
            print("data = " + str(data))
            for item in data:
                print(item.last_update)
        elif data == "indiaCases":
            data = indiaCases.query.all()
            print("data = " + str(data))
            for item in data:
                print(item.recovered)


        else:
            print("sorry no exiats")




    return "hii"





if __name__ == '__main__':
    db.create_all()
    app.run( debug=True   )


