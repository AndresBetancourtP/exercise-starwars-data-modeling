import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    first_name =Column(String(80), nullable=False)
    last_name =Column(String(80), nullable=False)
    created_at =Column(String(80))
    updated_at =Column(String(80))
    email =Column(String(80),unique=True, nullable=False) 

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(200))
    climate = Column(String(200))
    population = Column(Integer)
    orbital_period = Column(Integer)
    diameter= Column(Integer)

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name =  Column(String(200))
    birth_year = Column(Integer)
    gender = Column(String(200))
    height = Column(Integer)
    skin_color = Column(String(200))
    eye_color = Column(String(200))

class Favorites(Base): 
    __tablename__ = 'favorites'
    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    fav_planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    fav_character_id = Column(Integer, ForeignKey('character.character_id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')