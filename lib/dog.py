from models import Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, desc,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)

def create_table(base, engine):
    base.metadata.create_all(engine)

    # Session = sessionmaker(bind=engine)
    # session = Session()
    
def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(f"%{name}%"), Dog.breed == breed).first()

def update_breed(session, dog, breed):
    return session.query(Dog).update({Dog.breed: breed})