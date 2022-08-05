"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

from flask_wtf import FlaskForm

# from wtforms

app = Flask(__name__)

app.config['SECRET_KEY'] = "hunter2"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_home_page():
    """Show home page listing pets with name, photo, and availibility"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Show add pet form and handle adding pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name = name,
                  species = species,
                  photo_url = photo_url,
                  age = age,
                  notes = notes)

        db.session.add(pet)
        db.session.commit()


        flash(f"Added {name}")
        return redirect("/")

    else:
        return render_template(
            "add-pet.html", form=form)