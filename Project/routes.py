from flask.globals import session
from Project import app
from flask import render_template, request, redirect, url_for
from Project import models


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
# Login function to check the entered username and password is valid or not and navigate to user's page
def login():

    try:
        error = None
        if request.method == "POST":

            usr = request.form['username']
            pwd = request.form['password']

            # selecting all the users

            attempted_user = models.users.query.filter_by(
                username=usr) .first()

            # checking the user in the Database or not

            if attempted_user is None:

                if usr == "admin" and pwd == "admin@123":
                    return redirect(url_for('admin'))

                error = "User not exists please register !!!"
            # Checking the valid user and password
            elif attempted_user.username == usr and attempted_user.password == pwd:

                session['user'] = attempted_user.username
                session['user_id'] = attempted_user.user_id

                return redirect(url_for('users'))

            #Invalid user
            else:
                error = "Username or password is wrong"

        return render_template('login.html', error=error)
    except:
        #redirrecting in case of error
        return redirect(url_for('error'))


@app.route('/register', methods=["POST", "GET"])
# Register function to register new user and check the user already exits or not also checks validations for passwords
def register():
    try:

        error = None

        if request.method == "POST":

            # Passing the input values from the form

            nusr = request.form['newusername']
            npwd = request.form['newpassword']
            ncpwd = request.form['re_password']
            email = request.form['email']
            # checking the password and confirm password
            if npwd == ncpwd:
                #checking all the registered users
                register_user = models.users.query.filter_by(
                    username=nusr).first()
                if(register_user is None):
                    # If user doesnt exist add to DB
                    usrdetail = models.users(
                        username=nusr, emailid=email, password=npwd, confirm_password=ncpwd)
                    models.db.session.add(usrdetail)
                    models.db.session.commit()
                    return redirect(url_for('login'))

                else:
                    # Existing Users
                    error = 'User/email id already existing'

            else:
                # Password mismatch
                error = "Password mismatching"

        return render_template('register.html', error=error)
    except:
        return redirect(url_for('error'))

# User landing page


@app.route('/users')
def users():

    username = session.get('user', None)
    return render_template('user.html', usrname=username)


# Admin landing page
@app.route('/admin')
def admin():

    users = models.users.query.all()

    result = models.result_table.query.all()

    progress_val= models.progress_tracker.query.all()
    questions=models.question_table.query.all()

    #retriving the details from the db to admin page

    if(users is not None and result is not None and progress_val is not None):
        above_50 = 0
        above_70 = 0
        above_90 = 0
        total_100 = 0
        count1=0
        for i in range(0, len(result)):
            val = result[i].overall
            if(int(val) > 50):
                above_50 = above_50+1
            if(int(val) > 70):
                above_70 = above_70+1
            if(int(val) > 90):
                above_90 = above_90+1
            if(int(val) == 100):
                total_100 = total_100+1

        for j in range(0,len(progress_val)):
            ans= progress_val[j].progress
            ans=int(ans)
            
            
            if(ans == 100):
                count1= count1+1
            
        total_user = len(users)
        length=len(questions)

    else:
        return redirect(url_for('error'))

    return render_template('admin.html',len=length,ques=questions,completed=count1, admin="admin", count=total_user, val1=above_50, val2=above_70, val3=above_90, val4=total_100)


# Error landing page
@app.route('/error')
def error():
   return render_template('error.html')

# Material page is the content display page where the user navigates to diffrent content and save progress and navigating to assesment page


@app.route('/material', methods=["POST", "GET"])
def material():

    try:

        usrname = session.get('user', None)

        btn = "Start Learning"
        message = None
        progress1 = 0

        if request.method == "POST":
            # saving the progress of the content in the course
            prog = request.form['page']
            prog = int(prog)*10


            progress_val = models.progress_tracker(
                username=usrname, progress=prog)
            existing_users = models.progress_tracker.query.filter_by(
                username=usrname).first()

            # for  new user progress is saved 
            if existing_users is None:

                models.db.session.add(progress_val)
                models.db.session.commit()
                message = "Progress saved"
            # for existing user progress is deleted and saved  only if the old progress is less than new value
            elif int(existing_users.progress) < int(prog):

                models.db.session.delete(existing_users)

                models.db.session.add(progress_val)
                models.db.session.commit()
                message = "Progress Saved"

            else:

                pass

        value = models.progress_tracker.query.filter_by(
            username=usrname).first()
        # If the user has completed the quiz with 100% then the content is marked as completed
        progress1 = value.progress
        if(value is not None):
            progress1 = value.progress
            session['progress'] = progress1
            if(int(progress1) == 100):
                btn = "Completed"
            elif(int(progress1) > 0):
                btn = "Continue Learning"

        else:
            btn = "Start Learning"

        return render_template('material.html', username=usrname, msg=message, progress=progress1, button=btn)
    except:

        return render_template('material.html', username=usrname, msg=message, progress=progress1, button=btn)

# Question page for the assessments where question are retrived from DB and evaluated

@app.route('/questions/<string:id>', methods=["POST", "GET"])
def questions(id):

    try:
        values = models.question_table.query.all()

        prog = session.get('progress', None)

        if request.method == "POST":
            # retriving the selected values
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

          

            save_answers = models.evaluation_table(username=id, question1=answer1, question2=answer2, question3=answer3, question4=answer4,
                                                   question5=answer5, question6=answer6, question7=answer7, question8=answer8, question9=answer9, question10=answer10)
            existing_users = models.evaluation_table.query.filter_by(
                username=id).first()
            # if user is giving quiz for first time
            
            if existing_users is None:

                models.db.session.add(save_answers)
                models.db.session.commit()
            # if the user has already given the quiz

            else:
                models.db.session.delete(existing_users)

                models.db.session.add(save_answers)
                models.db.session.commit()

            answers = models.evaluation_table.query.filter_by(
                username=id).first()
            
            # Retriving the correct answers from the database
            crt_answers = models.question_table.query.all()
            point = 0
            cat1 = 0
            cat2 = 0
            cat3 = 0
            # adding the score for each category

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

            # adding the marks to the database

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
        return redirect(url_for('error'))

# Displaying the result from the questions and retriving feedback from database
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

    # selecting feedback from database
    feedback1 = models.feedback_table.query.filter_by(score=cat1).first()
    feedback2 = models.feedback_table.query.filter_by(score=cat2).first()
    feedback3 = models.feedback_table.query.filter_by(score=cat3).first()

    # categorizing the answers

    if(int(overall) > 75):
        overall = 100
    elif(int(overall) >= 50 and int(overall) <= 75):
        overall = 50
    elif(int(overall) > 0):
        overall = 25
    else:
        overall = 0

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
