from flask import Flask,request,render_template,redirect,url_for
from flask_restful import Resource, Api
app = Flask(__name__ )
api = Api(app)



@app.route('/',methods=["POST","GET"])
def index():
    return "hello"




if __name__ == '__main__':
    app.run( debug=True   )


