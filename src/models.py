import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)




class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    modelo = Column(String(250), nullable=False)
  



class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    




class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)




class FavoritosPersonajes(Base):
    __tablename__ = 'favoritos_personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    id = Column(Integer, primary_key=True)
    personaje_relacion = Column(Integer, ForeignKey('personajes.id'),nullable= False)
    usuario_relacion = Column(Integer, ForeignKey('usuarios.id'),nullable= False)
    personas = relationship(Personajes)
    usuarios= relationship(Usuarios)




class FavoritosVehiculos(Base):
    __tablename__ = 'favoritos_vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    id = Column(Integer, primary_key=True)
    vehiculo_relacion = Column(Integer, ForeignKey('vehiculos.id'),nullable= False)
    usuario_relacion = Column(Integer, ForeignKey('usuarios.id'),nullable= False)
    vehiculos = relationship(Vehiculos)
    usuarios= relationship(Usuarios)





class FavoritosPlanetas(Base):
    __tablename__ = 'favoritos_planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    id = Column(Integer, primary_key=True)
    planetas_relacion = Column(Integer, ForeignKey('planetas.id'),nullable= False)
    usuario_relacion = Column(Integer, ForeignKey('usuarios.id'),nullable= False)
    personas = relationship(Planetas)
    usuarios= relationship(Usuarios)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

