from datetime import datetime
from IntellFRS import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    __tablename__ = "user1"
    id         = db.Column(db.Integer,primary_key=True)
    name =       db.Column(db.String(50), unique=True, nullable=False)
    email =      db.Column(db.String(120), unique=True, nullable=False)
    mobile =     db.Column(db.BigInteger, nullable= False)
    cal_id =     db.Column(db.String(), unique=True, nullable=False)
    address =    db.Column(db.String(200), unique=True)
    image_file = db.Column(db.String(200), nullable=False, default='default.jpg')
    # Referer
    reg_no = db.relationship('Attendance', lazy=True)

    def __init__(self,name,mobile,cal_id,address,image_file,email):
        self.name = name
        self.mobile = mobile
        self.cal_id = cal_id
        self.email = email
        self.address = address
        self.image_file = image_file


    def __repr__(self):
        return "<User(id='%s', name='%s', email='%s', mobile='%s' cal_id='%s', address='%s')>" % (self.id, self.name, self.email,self.mobile,self.cal_id,self.address)
        #return f"User('{self.id}','{self.name}', '{self.email}', '{self.mobile}','{self.cal_id}', '{self.address}')"

class Attendance(db.Model):
    __tablename__ = "Attendance"
    id = db.Column(db.Integer, primary_key=True)
    presence = db.Column(db.String(8), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reg_no= db.Column(db.Integer,db.ForeignKey("user1.id"),nullable=False)


    def __repr__(self):
        #return  f"Attendance('{self.id}', '{self.presence}','{self.datetime}','{self.reg_no}')"
        return "<Attendance(id='%s', presence='%s', datetime='%s', reg_no='%s')>" % (self.id, self.presence, self.datetime,self.reg_no)



