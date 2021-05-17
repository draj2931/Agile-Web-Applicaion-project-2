from flask.globals import session
from Project import app
from flask import render_template, request, flash, redirect, url_for, jsonify, make_response
from Project import models
import sqlite3


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():

    try:
        error = None
        if request.method == "POST":

            usr = request.form['username']
            pwd = request.form['password']

            attempted_user = models.users.query.filter_by(
                username=usr) .first()

            user = None
            user_id = None
            if attempted_user is None:

                error = "User not exists please register !!!"

            elif attempted_user.username == usr and attempted_user.password == pwd:

                session['user'] = attempted_user.username
                session['user_id'] = attempted_user.user_id

                return redirect(url_for('users'))
            else:
                error = "Username or password is wrong"

        return render_template('login.html', error=error)
    except:
        return "ERROR"


@app.route('/register', methods=["POST", "GET"])
def register():
    try:
        error = None

        if request.method == "POST":
            print(1)
            nusr = request.form['newusername']
            npwd = request.form['newpassword']
            ncpwd = request.form['re_password']
            email = request.form['email']

            if npwd == ncpwd:

                register_user = models.users.query.filter_by(
                    emailid=email).first()
                if(register_user is None):
                    usrdetail = models.users(
                        username=nusr, emailid=email, password=npwd, confirm_password=ncpwd)
                    models.db.session.add(usrdetail)
                    models.db.session.commit()
                    return redirect(url_for('login'))

                else:
                    error = 'User/email id already existing'

            else:
                error = "Password mismatching"

        return render_template('register.html', error=error)
    except:
        return "error"


@app.route('/users')
def users():

    username = session.get('user', None)
    return render_template('user.html', usrname=username)


@app.route('/error')
def error():
   return render_template('error.html')


@app.route('/course')
def course():
    return render_template('course.html')


@app.route('/material', methods=["POST", "GET"])
def material():

    try:
        usrname = session.get('user', None)
        usrid = session.get('user_id', None)
        btn="Start Learning"
        message = None
        progress1=0
        
        if request.method == "POST":
            print("POST IN")
            prog = request.form['page']

            prog = int(prog)*10

            progress_val = models.progress_tracker(
                username=usrname, progress=prog)
            existing_users = models.progress_tracker.query.filter_by(
                username=usrname).first()

            if existing_users is None:

                models.db.session.add(progress_val)
                models.db.session.commit()
                message = "Progress saved"

            elif int(existing_users.progress) < int(prog):

                models.db.session.delete(existing_users)

                models.db.session.add(progress_val)
                models.db.session.commit()
                message = "Progress Saved"

            else:
                pass

        value = models.progress_tracker.query.filter_by(
            username=usrname).first()
        progress1= value.progress
        if(value is not None):
            progress1= value.progress
            session['progress'] = progress1
            if(int(progress1)==100):
                btn = "Completed"
            elif(int(progress1)>0):
                btn="Continue Learning"

        else:
            btn = "Start Learning"

        return render_template('material.html', username=usrname, msg=message, progress=progress1, button=btn)
    except:

        return render_template('material.html', username=usrname, msg=message, progress=progress1, button=btn)


@app.route('/questions/<string:id>', methods=["POST", "GET"])
def questions(id):

    try:
        values = models.question_table.query.all()

        prog = session.get('progress', None)

        if request.method == "POST":

            answer1 = request.form["0"]

            answer2 = request.form["1"]
            answer3 = request.form["2"]
            answer4 = request.form["3"]
            answer5 = request.form["4"]
            answer6 = request.form["5"]

            answer7 = request.form["6"]
            answer8 = request.form["7"]
            answer9 = request.form["8"]
            answer10 = request.form["9"]

            answer5 = request.form["4"]

            save_answers = models.evaluation_table(username=id, question1=answer1, question2=answer2, question3=answer3, question4=answer4,
                                                   question5=answer5, question6=answer6, question7=answer7, question8=answer8, question9=answer9, question10=answer10)
            existing_users = models.evaluation_table.query.filter_by(
                username=id).first()
            if existing_users is None:

                models.db.session.add(save_answers)
                models.db.session.commit()

            else:
                models.db.session.delete(existing_users)

                models.db.session.add(save_answers)
                models.db.session.commit()

            answers = models.evaluation_table.query.filter_by(
                username=id).first()
            crt_answers = models.question_table.query.all()
            point = 0
            cat1 = 0
            cat2 = 0
            cat3 = 0

            if(answers.question1 == crt_answers[0].Answers):
                point = point+1
                cat1 = cat1+1

            if(answers.question2 == crt_answers[1].Answers):
                point = point+1
                cat1 = cat1+1
            if(answers.question3 == crt_answers[2].Answers):
                point = point+1
                cat1 = cat1+1

            if(answers.question4 == crt_answers[3].Answers):
                cat2 = cat2+1
                point = point+1
            if(answers.question5 == crt_answers[4].Answers):
                point = point+1
                cat2 = cat2+1

            if(answers.question6 == crt_answers[5].Answers):
                point = point+1
                cat2 = cat2+1

            if(answers.question7 == crt_answers[6].Answers):
                point = point+1
                cat3 = cat3+1
            if(answers.question8 == crt_answers[7].Answers):
                point = point+1
                cat3 = cat3+1
            if(answers.question9 == crt_answers[8].Answers):
                point = point+1
                cat3 = cat3+1
            if(answers.question10 == crt_answers[9].Answers):
                point = point+1
                cat1 = cat1+1

            point = point*10
            cat1 = int(cat1)
            cat1 = round((cat1/4 * 100))

            cat2 = int(cat2)
            cat2 = round((cat2/3 * 100))

            cat3 = int(cat3)
            cat3 = round((cat3/3*100))

            save_marks = models.result_table(
                username=id, category1=cat1, category2=cat2, category3=cat3, overall=point)
            current_user = models.result_table.query.filter_by(
                username=id).first()

            if current_user is None:

                models.db.session.add(save_marks)
                models.db.session.commit()

            else:
                models.db.session.delete(current_user)

                models.db.session.add(save_marks)
                models.db.session.commit()

            session['cat1'] = cat1
            session['cat2'] = cat2
            session['cat3'] = cat3
            session['overall'] = point
            session['name'] = id

            return redirect(url_for('result'))

        return render_template('questions.html', progress=prog, len=len(values), items=values, username=id)

    except:
        return redirect(url_for('result'))


@app.route('/result')
def result():

    cat1 = session.get('cat1', None)
    cat2 = session.get('cat2', None)
    cat3 = session.get('cat3', None)
    overall = session.get('overall', None)
    total = session.get('overall', None)
    name = session.get('name', None)
    cat1_feedback = None
    cat2_feedback = None
    cat3_feedback = None
    general_feedback = None

    feedback1 = models.feedback_table.query.filter_by(score=cat1).first()
    feedback2 = models.feedback_table.query.filter_by(score=cat2).first()
    feedback3 = models.feedback_table.query.filter_by(score=cat3).first()

    if(int(overall) > 75):
        overall = 100
    elif(int(overall) >= 50 and int(overall) <= 75):
        overall = 50
    elif(int(overall)>0):
        overall = 25
    else:
        overall=0


    if(int(total) == 100):
        ex_user = models.progress_tracker.query.filter_by(
            username=name).first()
        progress = models.progress_tracker(username=name, progress=100)

        models.db.session.delete(ex_user)
        models.db.session.add(progress)
        models.db.session.commit()

    value = models.progress_tracker.query.filter_by(username=name).first()

    prog = value.progress

    gen_feedback = models.feedback_table.query.filter_by(score=overall).first()

    cat1_feedback = feedback1.feedback_1
    cat2_feedback = feedback2.feedback_2
    cat3_feedback = feedback3.feedback_3
    general_feedback = gen_feedback.overall_feedback

    return render_template("result.html", scores=total, progress=prog, user=name, val1=cat1, val2=cat2, val3=cat3, feed1=cat1_feedback, feed2=cat2_feedback, feed3=cat3_feedback, gen=general_feedback)
