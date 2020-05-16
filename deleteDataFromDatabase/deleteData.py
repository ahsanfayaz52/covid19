from flask import Blueprint
from flask import request

from Models import japanCases,covidApi,indiaCases
from Models import db


mod3 = Blueprint('deleteData',__name__)

@mod3.route( '/<data>',methods=["POST","GET"])
def deleteData(data):
    """
    this method is called when user send request to delete data from apis
    :param data
    :return a string showing how much rows are affected i.e deleted
    """

    show = "null"
    if request.method == "GET":
        if data == "japanCases":
            try:
                #delete all the rows from japanCases table
                rows = db.session.query(japanCases).delete()
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
                # delete all the rows from japanCases table
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
                # delete all the rows from japanCases table
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
