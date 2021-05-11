from Project import db

class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(64), nullable=False)
    emailid=db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(20),nullable=False)
    confirm_password=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class content_table(db.Model):
    content_id=db.Column(db.Integer,primary_key=True)
    content_name=db.Column(db.String(100),nullable=False)
    section1=db.Column(db.String(1000),nullable=False)
    section2=db.Column(db.String(1000),nullable=False)
    section3=db.Column(db.String(1000),nullable=False)
    section4=db.Column(db.String(1000),nullable=False)
# add pictures


