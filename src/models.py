import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(250))

class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer)

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))


class Starship(Base):
    __tablename__ = 'Starship'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    name = Column(String(250), nullable=False)
    consumables = Column(String(250))
    crew = Column(Integer)
    manufacturer = Column(String(250))
    passengers = Column(Integer)

class Favourites(Base):
    __tablename__ = 'Favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    person_id = Column(Integer, ForeignKey('Person.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('Starship.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('Planet.id'), nullable=True)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')