"""Seed file to make sample data"""
from email.mime import image
from app import app
from models import db, Pet

# Create all tables
db.drop_all()
db.create_all()
Pet.query.delete()

pets = [
    Pet(
        name="Mila",
        species="Dog",
        age=4,
        notes="Half Bernese, Half Golden Retriever",
        available=False,
        image_url="https://dogtime.com/assets/uploads/gallery/flat-coated-retriever-dogs-and-puppies/flat-coated-retriever-dogs-puppies-1.jpg"
    ),
    Pet(
        name="Mika",
        species="Dog",
        age=2,
        notes="Mila's best friend",
        image_url="https://allbigdogbreeds.com/wp-content/uploads/2015/05/Native-American-Indian-Dog-1.jpg"
    ),
    Pet(
        name="Scooter",
        species="Cat",
        age=16,
        notes="Megan's cat",
        image_url="https://i0.wp.com/ideasfornames.com/wp-content/uploads/2019/11/shutterstock_161633468.jpg?w=1000&ssl=1"
    ),
    Pet(
        name="Fin",
        species="Fish",
        age=1,
        notes="Blue saimese fighter",
        image_url="https://www.thesprucepets.com/thmb/prlNHRyw-NV4cS5X8jFZt14OdmI=/941x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/siamese-fighting-fish-bettas-1378308-hero-f459084da1414308accde7e21001906c.jpg"
    )
]

for pet in pets:
    db.session.add(pet)

db.session.commit()
