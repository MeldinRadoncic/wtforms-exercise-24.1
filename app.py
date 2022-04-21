"""Pet Adoption Agency."""


from flask import Flask,render_template,request,redirect,flash
from models import db, connect_db,Pet
from flask_toastr import Toastr
from form import PetForm,EditPetForm

# Connect DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0258@localhost:5432/adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


# Connecting Debug Toolbar
from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config[' DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()
# Connect toastr messages
toastr = Toastr(app)

# List all pets on home page
@app.route('/')
def home_page():
    pet = Pet.query.all()
    return render_template("show_pets.html", pet=pet)

# Handle add pet form
@app.route('/add', methods=["GET","POST"])
def add_pet_form():
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name = name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash("Good luck," f"{new_pet.name}")
        return redirect("/")
    else:
        return render_template('/add_pet_form.html', form=form)

# Show Pet info page
@app.route('/<int:pet_id_number>')
def pet_info(pet_id_number):
    pet = Pet.query.get(pet_id_number)

    # if pet id doesn't exist in DB throw message and redirect to add pet page
    if pet is None:
        flash("Pet Not Found")
        return redirect('/add')
    else:
        return render_template("pet-info.html", pet=pet)



# Edit Pet info
@app.route('/<int:id>/edit', methods=["GET","POST"])
def edit_pet(id):
    pet = Pet.query.get(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        
        flash(f'{pet.name} successfully updated')
        return redirect(f"/{pet.id}")

    else:
        return render_template('edit-pet-info.html',form=form,pet=pet)
        