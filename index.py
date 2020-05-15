from flask import Flask,request,render_template,redirect,url_for
from flask_restful import Resource, Api
import requests



import re
from bs4 import BeautifulSoup

from Models import theVirusTracker,covidApi,indiaCases
from Models import db,app




@app.route('/fetch/<data>',methods=["POST","GET"])
def covid19Stats(data):

    if request.method=="GET":



        url1 =  "https://api.thevirustracker.com/free-api?global=stats"
        url2 = "https://covid-api.com/api/reports/total?date=2020-04-15"
        url3 = "https://covid19-stats-api.herokuapp.com/api/v1/cases?country=India"

        if data == "virusTracker":
            result = extractDataFromApis(url1,"virusTracker" )

            return result
        if data == "covidApi":
            result = extractDataFromApis(url2, "covidApi")

            return result
        if data == "indiaCases":
            result = extractDataFromApis(url3, "indiaCases")
            return result
        else:
            return "no api available"









def extractDataFromApis(url,apiName):


    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        data = soup.find("p").text

        res = re.findall(r'\w+', data)
        values = re.split("[a-z]", str(res))

        numbers = re.findall(r'\d+', str(values))

        if apiName == "virusTracker":
            addDataToVirusTracker(numbers,url)

        if apiName == "covidApi":
            addDataToCovidApi(numbers)

        if apiName == "indiaCases":
            addDataToIndiaApi(numbers)


        return "Data is added successfully"

    except:
        return "Internal error occured"


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


    show = "null"
    if request.method == "GET":
        if data == "virusTracker":
            try:
                rows = db.session.query(theVirusTracker).delete()
                db.session.commit()
                print(rows)

                if rows == 1:
                    show  =  str(rows)  + " rows removed successfully"
                else:
                    show =  "no rows available"


            except:
                db.session.rollback()

        elif data == "covidApi":
            try:
                rows = db.session.query(covidApi).delete()
                db.session.commit()

                if rows != 0:
                    show  =  str(rows)  + " rows removed successfully"
                else:
                    show =  "no rows available"
            except:
                db.session.rollback()

        elif data == "indiaCases":
            try:
                rows = db.session.query(indiaCases).delete()
                db.session.commit()
                print(rows)
                if rows != 0:

                    show  =  str(rows)  + " rows removed successfully"
                else:
                    show =  "no rows available"


            except:
                db.session.rollback()

        else:
            return "sorry no api available"

    return show


@app.route('/getData/<data>',methods=["POST","GET"])
def getDataFromDatabase(data):
    result = "null"

    if request.method == "GET":

        if data == "virusTracker" :
            data = theVirusTracker.query.order_by(-theVirusTracker.id).all()
            print("data = " + str(data))
            for item in data :
                result = "total_cases = " + item.total_cases + "\ntotal_recovered = " + item.total_recovered + "\ntotal_unresolved = " + item.total_unresolved + "\ntotal_deaths = " + item.total_deaths + "\ntotal_new_cases_today = " + item.total_new_cases_today + "\ntotal_new_deaths_today = " + item.total_new_deaths_today + \
                         "\ntotal_active_cases = " + item.total_active_cases + "\ntotal_serious_cases = " + item.total_serious_cases + "\nactive = " + item.total_affected_countries + "\nsource = " + item.source

                break


        elif data == "covidApi":
            data = covidApi.query.order_by(-covidApi.id).all()

            for item in data:
                result = "date = "+item.date+"\nlast_update = "+item.last_update+"\nconfirmed = "+item.confirmed+"\nconfirmed_diff = "+item.confirmed_diff+"\ndeaths = "+item.deaths+"\ndeaths_diff = "+item.deaths_diff+\
                "\nrecovered = " + item.recovered + "\nrecovered_diff = " + item.recovered_diff + "\nactive = " + item.active + "\nactive_diff = " + item.active_diff + "\nfatality_rate = " + item.fatality_rate

                break
        elif data == "indiaCases":
            data = indiaCases.query.order_by(-indiaCases.id).all()

            for item in data:
                result = "confirmed cases = "+item.confirmed+"\nDeaths = "+item.deaths+"\nRecovered = "+item.recovered

                break


        else:
            print("sorry no exiats")




    return result





if __name__ == '__main__':
    db.create_all()
    app.run( debug=True   )


