from flask import Flask,request,render_template,redirect,url_for
from flask_restful import Resource, Api
import requests



import re
from bs4 import BeautifulSoup

from Models import theVirusTracker
from Models import db,app




@app.route('/fetch',methods=["POST","GET"])
def index():

    if request.method=="GET":


        total_cases = 0
        url =  "https://api.thevirustracker.com/free-api?global=stats"

        html_content =  requests.get(url).text
        soup = BeautifulSoup(html_content,"lxml")
        data = soup.find("p").text

        res = re.findall(r'\w+', data)
        values = re.split("[a-z]",str(res))

        numbers = re.findall(r'\d+', str(values))
        data = theVirusTracker(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5],
                           numbers[6], numbers[7], numbers[8], url)

        added = db.session.add(data)
        db.session.commit()
        print("total = "+str(numbers))





        return "added successfully"


@app.route('/delete/virusTracker',methods=["POST","GET"])
def delete():

    if request.method == "GET":
        try:
            rows = db.session.query(theVirusTracker).delete()
            db.session.commit()

            show = rows+" removed successfully"
        except:
            db.session.rollback()
            show = "no rows available"


        return show

@app.route('/getData/virusTracker',methods=["POST","GET"])
def getData():

    if request.method == "GET":
        data =  theVirusTracker.query.all()
        print("data = "+str(data))
        for item in data:
            print(item.total_cases)

    return "hii"





if __name__ == '__main__':
    db.create_all()
    app.run( debug=True   )


