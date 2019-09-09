from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:pineapple@123@localhost:15432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#db.init_app(app)
db.create_all()
db.session.commit()
#engine = create_engine('postgresql+psycopg2://postgres:pineapple@123@localhost:15432/postgres')
# metadata = Metadata()
# metadata.create_all(User)
# metadata.create_all(Attendance)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
	db.create_all()

from IntellFRS import routes
