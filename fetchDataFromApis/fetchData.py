from flask import Blueprint
from flask import request
import requests
import re
from bs4 import BeautifulSoup
from Models import japanCases,covidApi,indiaCases
from Models import db


mod1 = Blueprint('fetchData',__name__)



@mod1.route( '/<data>',methods=["POST","GET"])
def fetchData(data):
    """
    this method is called when user send request to extract new data from apis
    :param data
    :return a string showing wether data is added to database or some internal error is occured
    """

    if request.method == "GET":
        ### i have named the apis as japanCases, covidApi, indiaCases

        url1 = "https://covid19-japan-web-api.now.sh/api/v1/total"                   #japanCases
        url2 = "https://covid-api.com/api/reports/total?date=2020-04-15"             #covidApi
        url3 = "https://covid19-stats-api.herokuapp.com/api/v1/cases?country=India"  #indiaCases

        if data == "japanCases":
            result = extractDataFromApis(url1, "japanCases")

            return result
        if data == "covidApi":
            result = extractDataFromApis(url2, "covidApi")

            return result
        if data == "indiaCases":
            result = extractDataFromApis(url3, "indiaCases")
            return result
        else:
            return "no api available"


def extractDataFromApis(url, apiName):
    try:
        """
        this method is used to extract data from apis and call another methods to add data in particular database
        :param url, apiName 
        :return a string showing wether data is added to database or some internal error is occured
        """
        ###############    Extracting data from apis   ##############
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")

        data = soup.find("p").text


        #filtering data to get useful information only
        res = re.findall(r'\w+', data)
        values = re.split("[a-z]", str(res))

        numbers = re.findall(r'\d+', str(values))


		 
     

        if apiName == "japanCases":
            addDataToJapanCases(numbers)

        if apiName == "covidApi":
            addDataToCovidApi(numbers)

        if apiName == "indiaCases":
            addDataToIndiaApi(numbers)

        return "Data is added successfully"

    except:
        return "Internal error occured"


def addDataToJapanCases(numbers):
    """

     this method is used to add data to japanCases table
     :param list of numbers
     :return none



    """

    date = numbers[0]
    pcr = numbers[1]
    positive = numbers[2]
    symptom = numbers[3]
    symptomless = numbers[4]
    symptomConfirming = numbers[5]
    hospitalize = numbers[6]
    mild = numbers[7]
    severe = numbers[8]
    confirming = numbers[9]
    waiting = numbers[10]
    discharge = numbers[11]
    death = numbers[12]




    data = japanCases(date, pcr, positive, symptom, symptomless,
                           symptomConfirming, hospitalize, mild,severe, confirming,
                           waiting,discharge,death)

    db.session.add(data)
    db.session.commit()


def addDataToCovidApi(numbers):
    """

         this method is used to add data to covidApi table
         :param list of numbers
         :return none



        """
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
    """

         this method is used to add data to indiaCases table
         :param list of numbers
         :return none



        """
    confirmed = numbers[0]
    deaths = numbers[1]
    recovered = numbers[2]
    print(numbers)

    indiaApiData = indiaCases(confirmed, deaths, recovered)
    db.session.add(indiaApiData)
    db.session.commit()


