from Project import app
from flask import render_template,request
from Project import models

@app.route('/')
def index():
    return  render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def checklogin():

    usr = request.form['username']
    pwd = request.form['password']

    
    attempted_user= models.users.query.filter_by(username=usr).first()
    print(attempted_user)
    if attempted_user is None :
        return render_template("error.html")
    elif attempted_user.username == usr and attempted_user.password == pwd :
        return render_template('user.html',value=usr)
    else:
        return render_template('register.html')

@app.route('/register', methods=["POST","GET"])
def register():
    if request.method == "POST":
        nusr=request.form['newusername']
        npwd=request.form['newpassword']
        

        usrdetail=models.users(username=nusr,password=npwd)
        models.db.session.add(usrdetail)
        models.db.session.commit()
    

    return render_template('register.html')