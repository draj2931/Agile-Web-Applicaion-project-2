from enum import unique
from Project import db

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(64), nullable=False)
    emailid=db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.String(20),nullable=False)
    confirm_password=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class question_table(db.Model):
    question_id=db.Column(db.Integer,primary_key=True)
    question=db.Column(db.String(1000),nullable=False)
    option1=db.Column(db.String(1000),nullable=False)
    option2=db.Column(db.String(1000),nullable=False)
    option3=db.Column(db.String(1000),nullable=False)
    option4=db.Column(db.String(1000),nullable=False)
    
    Answers=db.Column(db.String(1000),nullable=False)

class evaluation_table(db.Model):
    evalid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    question1=db.Column(db.String(100),nullable=False)
    question2=db.Column(db.String(100),nullable=False)
    question3=db.Column(db.String(100),nullable=False)
    question4=db.Column(db.String(100),nullable=False)
    question5=db.Column(db.String(100),nullable=False)
    question6=db.Column(db.String(100),nullable=False)
    question7=db.Column(db.String(100),nullable=False)
    question8=db.Column(db.String(100),nullable=False)
    question9=db.Column(db.String(100),nullable=False)
    question10=db.Column(db.String(100),nullable=False)
   

class progress_tracker(db.Model):
    progress_id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    progress=db.Column(db.String(100),nullable=False)


class result_table(db.Model):
    result_id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    category1=db.Column(db.Integer,nullable=False)
    category2=db.Column(db.Integer,nullable=False)
    category3=db.Column(db.Integer,nullable=False)
    overall=db.Column(db.Integer,nullable=False)

class feedback_table(db.Model):
    feedback_id=db.Column(db.Integer,primary_key=True)
    score=db.Column(db.Integer,nullable=False)
    feedback_1=db.Column(db.String(500),nullable=False)
    feedback_2=db.Column(db.String(500),nullable=False)
    feedback_3=db.Column(db.String(500),nullable=False)
    overall_feedback=db.Column(db.String(500),nullable=False)



    


    


    



    






    


    



