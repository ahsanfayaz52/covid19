from flask import Flask

app = Flask(__name__ )
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///covid19Stats.db'
db =  SQLAlchemy(app)


from fetchDataFromApis.fetchData import mod1
from  getDataFromDatabase.getData import mod
from deleteDataFromDatabase.deleteData import mod3


app.register_blueprint ( mod1,url_prefix = "/fetch" )
app.register_blueprint ( mod, url_prefix = "/get"  )
app.register_blueprint ( mod3 , url_prefix = "/delete")







