import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Usuario)

class Personajes (Base):
    __tablename__ = 'Personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    type = Column(String(250))
    faccion = Column(String(250))
    raza = Column(String(250))
    gender = Column(String(250))

class Planetas (Base):
    __tablename__ = 'Planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    size = Column(String(250))
    temp = Column(String(250))
    color = Column(String(250))
    moon_number = Column(String(250))

class Vehiculos (Base):
    __tablename__ = 'Vehiculos'
    id = Column(Integer, primary_key=True)
    color = Column(String(250))
    model = Column(String(250))
    brand = Column(String(250))
    size = Column(Float(2))
    passengers = Column(Integer)

class Favorites (Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    vehicle_id = column(Integer, Foreignkey('vehiculo.id'))
    vehicle_favoritos = (relationship(Vehicles))
    user_id = column(Integer, ForeignKey('usuario.id'))
    user_favoritos = (relationship(usuario))
                                                    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
