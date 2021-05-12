from Project import app
from flask import render_template,request,flash,redirect,url_for
from Project import models

@app.route('/')
def index():
    return  render_template('home.html')



@app.route('/login', methods=['POST','GET'])
def login():

    if request.method =="POST":

        usr = request.form['username']
        pwd = request.form['password']
        attempted_user= models.users.query.filter_by(username=usr).first()

        print("---------------------")
        print(attempted_user)
        if attempted_user is None :
            
            return redirect(url_for('error'))
        elif attempted_user.username == usr and attempted_user.password == pwd :
            return redirect(url_for('users',value=usr))
        else:
            return redirect(url_for('register'))
    else:
        return render_template('login.html')
   
@app.route('/register', methods=["POST","GET"])
def register():
    if request.method == "POST":
        nusr=request.form['newusername']
        npwd=request.form['newpassword']
        ncpwd=request.form['re_password']
        email=request.form['email']

        usrdetail=models.users(username=nusr,emailid=email,password=npwd,confirm_password=ncpwd)
        models.db.session.add(usrdetail)
        models.db.session.commit()
        # check this route file where link above is not changing
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/users/<value>')
def users(value):
    return render_template('user.html',value1=value)

@app.route('/error')
def error():
   return render_template('error.html')
@app.route('/course')
def course():
    return render_template('course.html')
@app.route('/material')
def material():
    return render_template('material.html')