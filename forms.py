from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, TextAreaField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional, NumberRange,URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species")
    photo_url = URLField("photo link", validators=[URL(message='hi'),Optional()])
    age = IntegerField("Pet Age", validators=[NumberRange(0,30,'select age between 0-30'),Optional()])
    notes = TextAreaField("Additional notes")
    available = BooleanField()