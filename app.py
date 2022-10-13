from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "milaisthebestdogintheworld"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """Shows home page listing pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/<int:id>', methods=['GET'])
def pet_details(id):
    """Shows details about a specific pet"""
    pet = Pet.query.get_or_404(id)
    return render_template('details.html', pet=pet)


@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Shows a form to add a new pet"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species,
                  image_url=image_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet_form(id):
    """Shows a form to edit an existing pet"""
    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.image_url = form.image_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect(f'/{id}')
    else:
        return render_template('edit-pet.html', form=form)
