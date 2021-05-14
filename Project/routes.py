from Project import app
from flask import render_template,request,flash,redirect,url_for,jsonify,make_response
from Project import models
import sqlite3

@app.route('/')
def index():
    return  render_template('home.html')



@app.route('/login', methods=['POST','GET'])
def login():

    if request.method =="POST":

        usr = request.form['username']
        pwd = request.form['password']
        attempted_user= models.users.query.filter_by(username=usr).first()

       
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
@app.route('/material/<string:id>' , methods=["POST","GET"])
def material(id):

    if request.method == "POST":
        prog = request.form['completed']
        progress_val=models.progress_tracker(username=id,progress=prog)
        existing_users= models.progress_tracker.query.filter_by(username=id).first()
        if existing_users is None:
            models.db.session.add(progress_val)
            models.db.session.commit()
        elif int(existing_users.progress)< int(prog):
            models.db.session.delete(existing_users)
            
            models.db.session.add(progress_val)
            models.db.session.commit()
        else:
            pass
            

    return render_template('material.html',username=id)

@app.route('/questions/<string:id>',methods=["POST","GET"])
def questions(id):
    values=models.question_table.query.all()

    if request.method == "POST":
        
        answer1=request.form["0"]
        
        answer2=request.form["1"]
        answer3=request.form["2"]
        answer4=request.form["3"]
        print(answer4)

        answer5=request.form["4"]

        save_answers=models.evaluation_table(username=id,question1=answer1,question2=answer2,question3=answer3,question4=answer4,question5=answer5)
        existing_users= models.evaluation_table.query.filter_by(username=id).first()
        if existing_users is None:

            models.db.session.add(save_answers)
            models.db.session.commit()
            
        else:
            models.db.session.delete(existing_users)
            
            models.db.session.add(save_answers)
            models.db.session.commit()
          

        
        answers= models.evaluation_table.query.filter_by(username=id).first()
        crt_answers=models.question_table.query.all()
        point=0

  

        if(answers.question1 == crt_answers[0].Answers):
            point=point+1
        if(answers.question2 == crt_answers[1].Answers):
            point=point+1
        if(answers.question3 == crt_answers[2].Answers):
            point=point+1
        if(answers.question4 == crt_answers[3].Answers):
            point=point+1
        if(answers.question5 == crt_answers[4].Answers):
            point=point+1

        return redirect(url_for('result',score=point,name=id))


        

    
        

    
    return render_template('questions.html', len=len(values),items=values,username=id )


@app.route('/result/<int:score>/<string:name>')
def result(score,name):

    return render_template("result.html",scores=score,user=name)

