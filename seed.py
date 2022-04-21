from hashlib import algorithms_available
from app import db
from models import Pet

photo1="https://i.pinimg.com/564x/11/98/1c/11981cc3fd1d13e2583492397af8a62a.jpg"

db.drop_all()
db.create_all()

pet1 = Pet(name="Deni", species='Cat',age=5,photo_url=photo1,notes='Beutiful Cat',available=False)
pet2 = Pet(name="Blade", species='Dog',age=1,notes='I am so CUTE',available=True)

db.session.add(pet1)
db.session.add(pet2)
db.session.commit()