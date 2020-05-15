
from flask import request,Blueprint

from Models import japanCases,covidApi,indiaCases

mod = Blueprint('getData',__name__)

@mod.route('/<data>',methods=["POST","GET"])
def getData(data):
    result = "null"

    if request.method == "GET":

        if data == "japanCases" :
            data = japanCases.query.order_by(-japanCases.id).all()
            print("data = " + str(data))
            for item in data :
                result = "date = " + item.date + "\npcr = " + item.pcr + "\npositive = " + item.positive + "\nsymptom = " + item.symptom + "\nsymptomless = " + item.symptomless + "\nsymptomConfirming = " + item.symptomConfirming + \
                         "\nhospitalize = " + item.hospitalize + "\nmild = " + item.mild+ "\nsevere = " + item.severe + "\nconfirming = " + item.confirming + "\nwaiting = " + item.waiting+ "\ndischarge = " + item.discharge + "\ndeath = " + item.death

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
