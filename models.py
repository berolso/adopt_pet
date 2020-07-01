"""Models for Blogly."""
 
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
  '''connect to db'''
  db.app = app
  db.init_app(app)

class Pet(db.Model):
  '''pet class'''
  __tablename__ = 'pets'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(30), nullable=False)
  species = db.Column(db.String, nullable=False)
  photo_url = db.Column(db.String, default='https://images.unsplash.com/photo-1535930749574-1399327ce78f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2176&q=80')
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean)

  def __repr__(self):
	  return f'<User | {self.id} | {self.name} | {self.available}>'

