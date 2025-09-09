"""
Integration tests for database operations.

These tests demonstrate how to test complex database operations,
transactions, and model interactions.
"""

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from utils.enums import GeneroEnum
from tests.factories import AnimalFactory, PersonaFactory, ResponsableFactory, set_session_for_factories


@pytest.mark.integration
class TestDatabaseOperations:
    """Test database operations and transactions."""
    
    def test_create_complete_animal_with_responsable(self, db_session):
        """Test creating an animal with its complete responsable chain."""
        set_session_for_factories(db_session)
        
        # Import models
        from models.persona import Persona
        from models.responsable import Responsable
        from models.animal import Animal
        
        # Create complete chain: Persona -> Responsable -> Animal
        persona = Persona(
            dni="12345678",
            nombre="María",
            apellido="García",
            telefono="1234567890",
            genero=GeneroEnum.F,
            email="maria@email.com"
        )
        db_session.add(persona)
        db_session.flush()  # Get the ID without committing
        
        responsable = Responsable(
            persona_id=persona.id,
            aceptaRecordatorios=True
        )
        db_session.add(responsable)
        db_session.flush()
        
        animal = Animal(
            nombre="Milo",
            especie="Perro",
            raza="Golden Retriever",
            sexo=GeneroEnum.M,
            alergias="Ninguna",
            responsable_id=responsable.id
        )
        db_session.add(animal)
        db_session.commit()
        
        # Verify the complete chain
        assert persona.id is not None
        assert responsable.persona_id == persona.id
        assert animal.responsable_id == responsable.id
        
        # Test relationships
        assert responsable.persona == persona
        assert animal.responsable == responsable
        assert animal in responsable.animales
    
    def test_transaction_rollback_on_error(self, db_session):
        """Test that transactions are properly rolled back on errors."""
        set_session_for_factories(db_session)
        
        from models.persona import Persona
        
        # Create a valid persona first
        persona1 = PersonaFactory()
        db_session.commit()
        
        # Count initial personas
        initial_count = db_session.execute(
            select(Persona)
        ).scalars().all()
        initial_persona_count = len(initial_count)
        
        # Start a transaction that will fail
        try:
            persona2 = Persona(
                dni=persona1.dni,  # Duplicate DNI - will fail
                nombre="Duplicate",
                apellido="Person",
                genero=GeneroEnum.M
            )
            db_session.add(persona2)
            db_session.commit()
        except IntegrityError:
            db_session.rollback()
        
        # Verify no new persona was added
        final_count = db_session.execute(
            select(Persona)
        ).scalars().all()
        final_persona_count = len(final_count)
        
        assert final_persona_count == initial_persona_count
    
    def test_cascade_operations(self, db_session):
        """Test cascade operations between related models."""
        set_session_for_factories(db_session)
        
        # Create animal with responsable
        animal = AnimalFactory()
        responsable_id = animal.responsable_id
        db_session.commit()
        
        # Verify animal exists
        from models.animal import Animal
        from models.responsable import Responsable
        
        assert db_session.get(Animal, animal.id) is not None
        assert db_session.get(Responsable, responsable_id) is not None
        
        # Test soft delete of animal
        animal.borrado = True
        db_session.commit()
        
        # Animal should still exist but marked as deleted
        reloaded_animal = db_session.get(Animal, animal.id)
        assert reloaded_animal is not None
        assert reloaded_animal.borrado is True
        
        # Responsable should still exist
        assert db_session.get(Responsable, responsable_id) is not None
    
    def test_bulk_operations(self, db_session):
        """Test bulk create and update operations."""
        set_session_for_factories(db_session)
        
        # Bulk create personas
        personas = []
        for i in range(5):
            persona = PersonaFactory()
            personas.append(persona)
        
        db_session.commit()
        
        # Verify all were created
        from models.persona import Persona
        all_personas = db_session.execute(select(Persona)).scalars().all()
        assert len(all_personas) >= 5
        
        # Bulk update
        for persona in personas:
            persona.telefono = f"UPDATE-{persona.id}"
        
        db_session.commit()
        
        # Verify updates
        for persona in personas:
            db_session.refresh(persona)
            assert persona.telefono.startswith("UPDATE-")
    
    def test_complex_queries(self, db_session):
        """Test complex database queries."""
        set_session_for_factories(db_session)
        
        from models.animal import Animal
        from models.responsable import Responsable
        from models.persona import Persona
        
        # Create test data
        for i in range(3):
            AnimalFactory(
                especie="Perro" if i % 2 == 0 else "Gato",
                sexo=GeneroEnum.M if i % 2 == 0 else GeneroEnum.F
            )
        db_session.commit()
        
        # Query: Find all male dogs
        male_dogs = db_session.execute(
            select(Animal).where(
                Animal.especie == "Perro",
                Animal.sexo == GeneroEnum.M,
                Animal.borrado == False
            )
        ).scalars().all()
        
        for dog in male_dogs:
            assert dog.especie == "Perro"
            assert dog.sexo == GeneroEnum.M
            assert dog.borrado is False
        
        # Query with join: Find animals with their responsable's persona
        animals_with_responsables = db_session.execute(
            select(Animal, Responsable, Persona)
            .join(Responsable, Animal.responsable_id == Responsable.id)
            .join(Persona, Responsable.persona_id == Persona.id)
            .where(Animal.borrado == False)
        ).all()
        
        for animal, responsable, persona in animals_with_responsables:
            assert animal.responsable_id == responsable.id
            assert responsable.persona_id == persona.id
    
    def test_database_constraints(self, db_session):
        """Test that database constraints are properly enforced."""
        from models.animal import Animal
        
        # Test foreign key constraint
        with pytest.raises(IntegrityError):
            invalid_animal = Animal(
                nombre="Huérfano",
                especie="Perro",
                sexo=GeneroEnum.M,
                alergias="Ninguna",
                responsable_id=99999  # Non-existent responsable
            )
            db_session.add(invalid_animal)
            db_session.commit()
        
        db_session.rollback()
    
    def test_concurrent_operations_simulation(self, db_session):
        """Simulate concurrent operations that might occur in production."""
        set_session_for_factories(db_session)
        
        # Create base data
        animal = AnimalFactory()
        db_session.commit()
        
        # Simulate concurrent updates
        animal_id = animal.id
        
        # First "session" updates name
        animal.nombre = "Updated by Session 1"
        
        # Simulate another session trying to update the same animal
        # In real concurrency, this would be another session
        from models.animal import Animal
        same_animal = db_session.get(Animal, animal_id)
        same_animal.color = "Updated by Session 2"
        
        # Both should succeed since they update different fields
        db_session.commit()
        
        # Verify both updates
        db_session.refresh(animal)
        assert animal.nombre == "Updated by Session 1"
        assert animal.color == "Updated by Session 2"
    
    def test_data_integrity_across_models(self, db_session):
        """Test data integrity is maintained across related models."""
        set_session_for_factories(db_session)
        
        # Create animal with all relationships
        animal = AnimalFactory()
        original_responsable_id = animal.responsable_id
        db_session.commit()
        
        # Verify integrity before changes
        assert animal.responsable is not None
        assert animal.responsable.persona is not None
        
        # Try to change responsable
        new_responsable = ResponsableFactory()
        db_session.commit()
        
        animal.responsable_id = new_responsable.id
        db_session.commit()
        
        # Verify new relationship
        db_session.refresh(animal)
        assert animal.responsable_id == new_responsable.id
        assert animal.responsable == new_responsable
        
        # Verify old responsable still exists
        from models.responsable import Responsable
        old_responsable = db_session.get(Responsable, original_responsable_id)
        assert old_responsable is not None