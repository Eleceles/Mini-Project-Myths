from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LocationForm(FlaskForm):
    name = StringField("Location Name", validators = [DataRequired()])
    submit = SubmitField("Add Location")

class MythForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    character = StringField("Character Name", validators = [DataRequired()])
    story = StringField("Story Name", validators = [DataRequired()])
    location = SelectField("Location Origen", choices=[])
    submit = SubmitField("Add Myth")