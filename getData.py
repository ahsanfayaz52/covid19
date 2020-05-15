
from flask import request,Blueprint

from Models import theVirusTracker,covidApi,indiaCases

mod = Blueprint('getData',__name__)

@mod.route('/<data>',methods=["POST","GET"])
def getData(data):
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
