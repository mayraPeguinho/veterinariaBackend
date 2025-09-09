"""
Test data factories using Factory Boy.

This module provides factories for creating test instances of model objects
with realistic data for testing purposes.
"""

import factory
from factory.alchemy import SQLAlchemyModelFactory
from datetime import date, datetime
from sqlalchemy.orm import sessionmaker

from utils.enums import GeneroEnum

class BaseFactory(SQLAlchemyModelFactory):
    """Base factory class for SQLAlchemy models."""
    
    class Meta:
        abstract = True
        sqlalchemy_session_persistence = "commit"

class PersonaFactory(BaseFactory):
    """Factory for creating Persona test instances."""
    
    class Meta:
        model = "models.persona.Persona"
    
    dni = factory.Sequence(lambda n: f"{n:08d}")
    nombre = factory.Faker("first_name")
    apellido = factory.Faker("last_name")
    telefono = factory.Faker("phone_number")
    genero = factory.Faker("enum", enum_cls=GeneroEnum)
    direccion = factory.Faker("address")
    email = factory.Faker("email")

class ResponsableFactory(BaseFactory):
    """Factory for creating Responsable test instances."""
    
    class Meta:
        model = "models.responsable.Responsable"
    
    aceptaRecordatorios = factory.Faker("boolean")
    borrado = False
    persona = factory.SubFactory(PersonaFactory)
    fecha_creacion = factory.LazyFunction(datetime.now)

class AnimalFactory(BaseFactory):
    """Factory for creating Animal test instances."""
    
    class Meta:
        model = "models.animal.Animal"
    
    nombre = factory.Faker("first_name")
    especie = factory.Faker("random_element", elements=("Perro", "Gato", "Conejo", "Hamster"))
    raza = factory.Faker("word")
    color = factory.Faker("color_name")
    peso = factory.Faker("random_element", elements=("5kg", "10kg", "15kg", "20kg"))
    tamaño = factory.Faker("random_element", elements=("Pequeño", "Mediano", "Grande"))
    temperamento = factory.Faker("random_element", elements=("Tranquilo", "Activo", "Agresivo", "Tímido"))
    sexo = factory.Faker("enum", enum_cls=GeneroEnum)
    alergias = factory.Faker("text", max_nb_chars=200)
    fecha_nacimiento = factory.Faker("date_of_birth", minimum_age=0, maximum_age=20)
    fecha_fallecimiento = None
    borrado = False
    responsable = factory.SubFactory(ResponsableFactory)
    fecha_creacion = factory.LazyFunction(datetime.now)

class VeterinariaFactory(BaseFactory):
    """Factory for creating Veterinaria test instances."""
    
    class Meta:
        model = "models.veterinaria.Veterinaria"
    
    nombre = factory.Faker("company")
    direccion = factory.Faker("address")
    telefono = factory.Faker("phone_number")
    email = factory.Faker("company_email")
    instagram = factory.Faker("user_name")

class PermisoFactory(BaseFactory):
    """Factory for creating Permiso test instances."""
    
    class Meta:
        model = "models.permiso.Permiso"
    
    nombre = factory.Faker("word")

def set_session_for_factories(session):
    """Set the database session for all factories."""
    BaseFactory._meta.sqlalchemy_session = session
    PersonaFactory._meta.sqlalchemy_session = session
    ResponsableFactory._meta.sqlalchemy_session = session
    AnimalFactory._meta.sqlalchemy_session = session
    VeterinariaFactory._meta.sqlalchemy_session = session
    PermisoFactory._meta.sqlalchemy_session = session