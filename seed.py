
from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
pet1 = Pet(name='Paul', species="cat",age=5,available=True)
pet2 = Pet(name='Dane', species="dog",age=5,available=True)
pet3 = Pet(name='Gabe', species="porcupine",age=5,available=False)

db.session.add_all([pet1,pet2,pet3])

# Commit--otherwise, this never gets saved!
db.session.commit()
