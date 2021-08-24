from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/example'

db = SQLAlchemy(app)

class Person(db.Model):
	__tablename__ = 'Persons'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route ('/')
person = Persons.query.first()
def index()
	return ('Hello' + person.name)