"""Seed file to make sample data"""
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
        notes="Half Bernese, Half Golden Retriever"
    )
]

for pet in pets:
    db.session.add(pet)

db.session.commit()
