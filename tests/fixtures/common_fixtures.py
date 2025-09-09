"""
Test fixtures for common test data scenarios.

This module provides pre-configured fixtures for common test scenarios
in the veterinary application.
"""

import pytest
from datetime import date, datetime

from utils.enums import GeneroEnum
from tests.factories import (
    PersonaFactory, ResponsableFactory, AnimalFactory, 
    VeterinariaFactory, PermisoFactory, set_session_for_factories
)


@pytest.fixture
def sample_persona(db_session):
    """Create a sample persona for testing."""
    set_session_for_factories(db_session)
    
    from models.persona import Persona
    
    persona = Persona(
        dni="12345678",
        nombre="Juan Carlos",
        apellido="Pérez García",
        telefono="+54911234567",
        genero=GeneroEnum.M,
        direccion="Av. Corrientes 1234, CABA",
        email="juan.perez@email.com"
    )
    
    db_session.add(persona)
    db_session.commit()
    return persona


@pytest.fixture
def sample_responsable(db_session, sample_persona):
    """Create a sample responsable linked to a persona."""
    from models.responsable import Responsable
    
    responsable = Responsable(
        persona_id=sample_persona.id,
        aceptaRecordatorios=True
    )
    
    db_session.add(responsable)
    db_session.commit()
    return responsable


@pytest.fixture
def sample_animal(db_session, sample_responsable):
    """Create a sample animal with a responsable."""
    from models.animal import Animal
    
    animal = Animal(
        nombre="Milo",
        especie="Perro",
        raza="Golden Retriever",
        color="Dorado",
        peso="25kg",
        tamaño="Grande",
        temperamento="Tranquilo",
        sexo=GeneroEnum.M,
        alergias="Polen, ácaros",
        fecha_nacimiento=date(2020, 3, 15),
        responsable_id=sample_responsable.id
    )
    
    db_session.add(animal)
    db_session.commit()
    return animal


@pytest.fixture
def sample_veterinaria(db_session):
    """Create a sample veterinaria."""
    from models.veterinaria import Veterinaria
    
    veterinaria = Veterinaria(
        nombre="Clínica Veterinaria San Martín",
        direccion="Av. San Martín 567, CABA",
        telefono="+54114567890",
        email="info@clinicasanmartin.com",
        instagram="@clinicasanmartin"
    )
    
    db_session.add(veterinaria)
    db_session.commit()
    return veterinaria


@pytest.fixture
def sample_permissions(db_session):
    """Create sample permissions for testing."""
    set_session_for_factories(db_session)
    
    permissions = [
        PermisoFactory(nombre="READ_ANIMALS"),
        PermisoFactory(nombre="WRITE_ANIMALS"),
        PermisoFactory(nombre="DELETE_ANIMALS"),
        PermisoFactory(nombre="READ_RESPONSABLES"),
        PermisoFactory(nombre="WRITE_RESPONSABLES"),
    ]
    
    db_session.commit()
    return permissions


@pytest.fixture
def multiple_animals(db_session):
    """Create multiple animals for testing pagination, filtering, etc."""
    set_session_for_factories(db_session)
    
    animals = []
    especies = ["Perro", "Gato", "Conejo"]
    sexos = [GeneroEnum.M, GeneroEnum.F]
    
    for i in range(10):
        animal = AnimalFactory(
            nombre=f"Animal {i+1}",
            especie=especies[i % len(especies)],
            sexo=sexos[i % len(sexos)]
        )
        animals.append(animal)
    
    db_session.commit()
    return animals


@pytest.fixture
def complete_family_scenario(db_session):
    """Create a complete family scenario with multiple pets."""
    set_session_for_factories(db_session)
    
    # Create family members
    from models.persona import Persona
    from models.responsable import Responsable
    from models.animal import Animal
    
    # Father
    padre = Persona(
        dni="11111111",
        nombre="Carlos",
        apellido="González",
        genero=GeneroEnum.M,
        telefono="+54911111111",
        email="carlos@family.com"
    )
    db_session.add(padre)
    db_session.flush()
    
    responsable_padre = Responsable(
        persona_id=padre.id,
        aceptaRecordatorios=True
    )
    db_session.add(responsable_padre)
    db_session.flush()
    
    # Mother  
    madre = Persona(
        dni="22222222",
        nombre="María",
        apellido="González",
        genero=GeneroEnum.F,
        telefono="+54922222222",
        email="maria@family.com"
    )
    db_session.add(madre)
    db_session.flush()
    
    responsable_madre = Responsable(
        persona_id=madre.id,
        aceptaRecordatorios=False
    )
    db_session.add(responsable_madre)
    db_session.flush()
    
    # Family pets
    dog = Animal(
        nombre="Rocky",
        especie="Perro",
        raza="Labrador",
        sexo=GeneroEnum.M,
        alergias="Ninguna",
        responsable_id=responsable_padre.id
    )
    
    cat = Animal(
        nombre="Luna",
        especie="Gato", 
        raza="Siamés",
        sexo=GeneroEnum.F,
        alergias="Polen",
        responsable_id=responsable_madre.id
    )
    
    rabbit = Animal(
        nombre="Copito",
        especie="Conejo",
        sexo=GeneroEnum.M,
        alergias="Ninguna",
        responsable_id=responsable_padre.id  # Father has two pets
    )
    
    db_session.add_all([dog, cat, rabbit])
    db_session.commit()
    
    return {
        "padre": padre,
        "madre": madre,
        "responsable_padre": responsable_padre,
        "responsable_madre": responsable_madre,
        "pets": [dog, cat, rabbit]
    }


@pytest.fixture
def animals_with_medical_history(db_session):
    """Create animals with simulated medical history."""
    set_session_for_factories(db_session)
    
    # Create animals with different medical scenarios
    healthy_animal = AnimalFactory(
        nombre="Healthy",
        alergias="Ninguna"
    )
    
    allergic_animal = AnimalFactory(
        nombre="Allergic",
        alergias="Polen, ácaros, alimentos con pollo"
    )
    
    senior_animal = AnimalFactory(
        nombre="Senior",
        fecha_nacimiento=date(2010, 1, 1),  # Old animal
        alergias="Ninguna"
    )
    
    deceased_animal = AnimalFactory(
        nombre="Deceased",
        fecha_fallecimiento=date(2023, 6, 15)
    )
    
    db_session.commit()
    
    return {
        "healthy": healthy_animal,
        "allergic": allergic_animal, 
        "senior": senior_animal,
        "deceased": deceased_animal
    }


@pytest.fixture
def database_with_sample_data(db_session):
    """Populate database with comprehensive sample data."""
    set_session_for_factories(db_session)
    
    # Create veterinarias
    veterinarias = [
        VeterinariaFactory(nombre="Clínica Norte"),
        VeterinariaFactory(nombre="Hospital Veterinario Central"),
        VeterinariaFactory(nombre="Consultorio Dr. García")
    ]
    
    # Create permissions
    permissions = [
        PermisoFactory(nombre="ADMIN"),
        PermisoFactory(nombre="VETERINARIO"),
        PermisoFactory(nombre="ASISTENTE"),
        PermisoFactory(nombre="RECEPCIONISTA")
    ]
    
    # Create multiple personas and responsables
    responsables = []
    for i in range(5):
        persona = PersonaFactory()
        responsable = ResponsableFactory(persona=persona)
        responsables.append(responsable)
    
    # Create animals for each responsable
    animals = []
    for responsable in responsables:
        num_pets = (responsable.id % 3) + 1  # 1-3 pets per responsable
        for j in range(num_pets):
            animal = AnimalFactory(responsable=responsable)
            animals.append(animal)
    
    db_session.commit()
    
    return {
        "veterinarias": veterinarias,
        "permissions": permissions,
        "responsables": responsables,
        "animals": animals
    }


@pytest.fixture
def edge_case_data(db_session):
    """Create edge case scenarios for testing."""
    set_session_for_factories(db_session)
    
    from models.persona import Persona
    from models.responsable import Responsable
    from models.animal import Animal
    
    # Minimum length names
    min_persona = Persona(
        dni="99999999",
        nombre="A",
        apellido="B", 
        genero=GeneroEnum.INDETERMINADO
    )
    db_session.add(min_persona)
    db_session.flush()
    
    min_responsable = Responsable(
        persona_id=min_persona.id,
        aceptaRecordatorios=False
    )
    db_session.add(min_responsable)
    db_session.flush()
    
    # Animal with minimal data
    min_animal = Animal(
        nombre="X",
        especie="Y",
        sexo=GeneroEnum.INDETERMINADO,
        alergias="",
        responsable_id=min_responsable.id
    )
    db_session.add(min_animal)
    
    # Animal with maximum data
    max_animal = AnimalFactory(
        nombre="A" * 50,  # Max length name
        alergias="A" * 200,  # Max length allergies
        responsable=min_responsable
    )
    
    db_session.commit()
    
    return {
        "min_persona": min_persona,
        "min_responsable": min_responsable,
        "min_animal": min_animal,
        "max_animal": max_animal
    }