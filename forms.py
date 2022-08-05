from ast import In
from tokenize import String
from flask_wtf import FlaskForm

from wtforms import StringField, SelectField, TextAreaField, BooleanField

from wtforms.validators import InputRequired, Optional, URL

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    """ Form for adding a new pet """

    name = StringField("Pet name: ",
                        validators=[InputRequired()])

    species = SelectField("Species: ", choices=[("cat", "Cat"),
                                        ("dog", "Dog"),
                                        ("porcupine", "Porcupine")],
                        validators=[InputRequired()])

    photo_url = StringField("Photo URL: ",
                             validators=[Optional(), URL()])

    age = SelectField("Age: ", choices=[("baby", "Baby"),
                                        ("young", "Young"),
                                        ("adult", "Adult"),
                                        ("senior", "Senior")],
                        validators=[InputRequired()])

    notes = TextAreaField("Notes: ", validators=[Optional()])

class EditPetForm(FlaskForm):
    """ Form for editing an existing pet """

    photo_url = StringField("Photo URL: ",
                             validators=[Optional(), URL()])

    notes = TextAreaField("Notes: ", validators=[Optional()]) # if doing optional, add length or something

    available = BooleanField("Available: ")