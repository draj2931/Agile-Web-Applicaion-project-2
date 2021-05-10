from Project import db

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String(64), nullable=False)
    emailid=db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(20),nullable=False)
    confirm_password=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

