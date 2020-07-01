from flask import Flask, request, redirect, render_template, url_for, flash
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

from forms import AddPetForm

# custom 404
@app.errorhandler(404)
def page_not_found(e):
  '''custom 404'''
  # note that we set the 404 status explicitly
  return render_template('404.html'), 404

@app.route('/')
def index():
  '''home page'''
  return redirect('/pets')

@app.route('/pets')
def pets_list():
  '''list all pets page'''
  pets = Pet.query.all()
  return render_template('pets.html', pets=pets) 

@app.route('/adopted')
def adopted_list():
  '''list adopted pets page'''
  pets = Pet.query.filter_by(available=False)
  return render_template('adopted.html', pets=pets) 

@app.route('/pets/add', methods=['GET','POST'])
def new_pet():
  '''add new pet page'''
  form = AddPetForm()
  form.species.choices = [('Dog','Dog'),('Cat','Cat'),('Porcupine','Porcupine')]
  if form.validate_on_submit():
    data = {k: v for k, v in form.data.items() if k != "csrf_token"}
    new_pet = Pet(**data)
    # name = form.name.data
    # species = form.species.data
    # photo_url = form.photo_url.data
    # age = form.age.data
    # notes = form.notes.data
    # available = form.available.data
    # new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
    db.session.add(new_pet)
    db.session.commit()

    flash(f'added {new_pet.name}')
    return redirect('/pets')
  else:
    return render_template('add_pet.html', form=form)

@app.route('/pets/<int:pet_id>/edit', methods=['GET','POST'])
def edit_pet(pet_id):
  '''edit pet page'''
  pet = Pet.query.get_or_404(pet_id)
  form = AddPetForm(obj=pet)
  form.species.choices = [('dog','Dog'),('cat','Cat'),('porcupine','Porcupine')]
  if form.validate_on_submit():
    pet.name = form.name.data
    pet.species = form.species.data
    pet.photo_url = form.photo_url.data
    pet.age = form.age.data
    pet.notes = form.notes.data
    pet.available = form.available.data
    db.session.commit()
    flash(f'updated {pet.name}','success')
    return redirect(f'/pets/{pet.id}')
  else:
    return render_template('edit_pet.html', form=form, pet=pet)

@app.route('/pets/<int:pet_id>/')
def show_pet(pet_id):
  '''show pet page'''
  pet = Pet.query.get_or_404(pet_id)
  return render_template('pet.html', pet=pet)
  