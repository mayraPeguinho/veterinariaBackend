"""
Unit tests for the Animal model.

These tests demonstrate how to test SQLAlchemy models in isolation,
including validation, relationships, and business logic.
"""

import pytest
from datetime import date, datetime
from sqlalchemy.exc import IntegrityError

from utils.enums import GeneroEnum
from tests.factories import AnimalFactory, ResponsableFactory, set_session_for_factories


@pytest.mark.unit
class TestAnimalModel:
    """Test cases for the Animal model."""
    
    def test_animal_creation_with_required_fields(self, db_session):
        """Test that an animal can be created with only required fields."""
        set_session_for_factories(db_session)
        
        # Create a responsable first
        responsable = ResponsableFactory()
        db_session.commit()
        
        # Import here to avoid circular imports with mocked DATABASE_URL
        from models.animal import Animal
        
        animal = Animal(
            nombre="Rex",
            especie="Perro",
            sexo=GeneroEnum.M,
            alergias="Ninguna",
            responsable_id=responsable.id
        )
        
        db_session.add(animal)
        db_session.commit()
        
        assert animal.id is not None
        assert animal.nombre == "Rex"
        assert animal.especie == "Perro"
        assert animal.sexo == GeneroEnum.M
        assert animal.alergias == "Ninguna"
        assert animal.responsable_id == responsable.id
        assert animal.borrado is False  # Default value
    
    def test_animal_creation_with_all_fields(self, db_session):
        """Test animal creation with all optional fields."""
        set_session_for_factories(db_session)
        
        responsable = ResponsableFactory()
        db_session.commit()
        
        from models.animal import Animal
        
        animal = Animal(
            nombre="Luna",
            especie="Gato",
            raza="Siamés",
            color="Gris",
            peso="4kg",
            tamaño="Mediano",
            temperamento="Tranquilo",
            sexo=GeneroEnum.F,
            alergias="Polen",
            fecha_nacimiento=date(2020, 5, 15),
            responsable_id=responsable.id
        )
        
        db_session.add(animal)
        db_session.commit()
        
        assert animal.raza == "Siamés"
        assert animal.color == "Gris"
        assert animal.peso == "4kg"
        assert animal.tamaño == "Mediano"
        assert animal.temperamento == "Tranquilo"
        assert animal.fecha_nacimiento == date(2020, 5, 15)
    
    def test_animal_requires_responsable(self, db_session):
        """Test that an animal cannot be created without a responsable."""
        from models.animal import Animal
        
        animal = Animal(
            nombre="Sin Dueño",
            especie="Perro",
            sexo=GeneroEnum.M,
            alergias="Ninguna"
        )
        
        db_session.add(animal)
        
        with pytest.raises(IntegrityError):
            db_session.commit()
    
    def test_animal_relationship_with_responsable(self, db_session):
        """Test the relationship between Animal and Responsable."""
        set_session_for_factories(db_session)
        
        animal = AnimalFactory()
        db_session.commit()
        
        # Test that the relationship works
        assert animal.responsable is not None
        assert animal.responsable.id == animal.responsable_id
        assert animal in animal.responsable.animales
    
    def test_animal_soft_delete(self, db_session):
        """Test the soft delete functionality."""
        set_session_for_factories(db_session)
        
        animal = AnimalFactory()
        db_session.commit()
        
        # Soft delete
        animal.borrado = True
        db_session.commit()
        
        assert animal.borrado is True
        # Animal still exists in database but marked as deleted
        assert animal.id is not None
    
    def test_animal_fecha_creacion_auto_set(self, db_session):
        """Test that fecha_creacion is automatically set."""
        set_session_for_factories(db_session)
        
        before_creation = datetime.now()
        animal = AnimalFactory()
        db_session.commit()
        after_creation = datetime.now()
        
        assert animal.fecha_creacion is not None
        assert before_creation <= animal.fecha_creacion <= after_creation
    
    def test_animal_fecha_modificacion_on_update(self, db_session):
        """Test that fecha_modificacion is set when updating."""
        set_session_for_factories(db_session)
        
        animal = AnimalFactory()
        db_session.commit()
        
        # Initially, modification date should be None
        assert animal.fecha_modificacion is None
        
        # Update the animal
        animal.nombre = "Nuevo Nombre"
        db_session.commit()
        
        # Now modification date should be set
        assert animal.fecha_modificacion is not None
    
    def test_animal_factory(self, db_session):
        """Test that the AnimalFactory creates valid animals."""
        set_session_for_factories(db_session)
        
        animal = AnimalFactory()
        db_session.commit()
        
        assert animal.id is not None
        assert animal.nombre is not None
        assert animal.especie in ("Perro", "Gato", "Conejo", "Hamster")
        assert animal.sexo in [GeneroEnum.M, GeneroEnum.F, GeneroEnum.INDETERMINADO]
        assert animal.responsable is not None
        assert animal.borrado is False
    
    def test_multiple_animals_same_responsable(self, db_session):
        """Test that a responsable can have multiple animals."""
        set_session_for_factories(db_session)
        
        responsable = ResponsableFactory()
        animal1 = AnimalFactory(responsable=responsable)
        animal2 = AnimalFactory(responsable=responsable)
        db_session.commit()
        
        assert len(responsable.animales) == 2
        assert animal1 in responsable.animales
        assert animal2 in responsable.animales