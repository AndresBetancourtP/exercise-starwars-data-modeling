import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    # date_subs = Column(DateTime, nullable=False)


class Characters (Base): 
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birthday_year = Column(Integer, nullable=False)
    Gender = Column(String(6), nullable=False)
    Height = Column(Integer, nullable=False)
    Skin_color = Column(String(200), nullable=False)
    Eye_color = Column(String(200), nullable=False)


class Planets (Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)


class Vehicles (Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)


class Fav_Characters (Base):
    __tablename__ = "fav_characters"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

class Fav_Planets (Base):
    __tablename__ = "fav_planets"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)

class Fav_Vehicles (Base):
    __tablename__ = "fav_vehicles"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')