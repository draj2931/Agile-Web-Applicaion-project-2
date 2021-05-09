from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agile.db'

db = SQLAlchemy(app)

from Project import routes


 



