from tokenize import Number
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,IntegerField,SelectField,TextAreaField
from wtforms.validators import InputRequired,InputRequired,Optional,URL,NumberRange,Length

# Add Pet wtform
class PetForm(FlaskForm):
    name = StringField("Pet name", validators =[InputRequired()])
    species = SelectField("Species", choices=[("Cat","CAT"), ("Dog","DOG"), ("Porcupine","PORCUPINE")])
    photo_url = StringField("Photo URL", validators = [Optional(), URL(require_tld=True, message="Enter valid URL")])
    age = IntegerField("Age",validators=[Optional(), NumberRange(min=0, max=30, message="Age must be from 0-30")])
    notes = TextAreaField("Notes", validators = [Length(min=4), Optional()])
    


# Handling EditPetForm
# Allow User to update img,age,notes and availability
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField("Age", validators=[Optional(),NumberRange(min=0,max=30,
    message="Age must be from 0-30")])

    notes = TextAreaField(
        "Notes",
        validators=[Optional(), Length(min=4)],
    )

    available = BooleanField("Available?")
    






