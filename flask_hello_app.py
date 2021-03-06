from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
	__tablename__ = 'persons'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	
	#the next line of the code is use for debuggin in the python terminal 
	def __repr__(self):
		return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route ('/')
person = Person.query.first()

def index():
	return ('Hello' + person.name)