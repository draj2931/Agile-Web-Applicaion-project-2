from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///agile.db'
db = SQLAlchemy(app)



class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),nullable=False,unique=True)
    password=db.Column(db.String(length=30),nullable=False,unique=True)



@app.route('/')
@app.route('/index')
def index():
    return  render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')  





if __name__=="__main__":
    app.run(debug=True)

