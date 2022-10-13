from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL


class PetForm(FlaskForm):

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    image_url = URLField("Image URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
