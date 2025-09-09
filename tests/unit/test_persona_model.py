"""
Unit tests for the Persona model.

These tests demonstrate validation, constraints, and relationships
for the Persona model.
"""

import pytest
from sqlalchemy.exc import IntegrityError

from utils.enums import GeneroEnum
from tests.factories import PersonaFactory, set_session_for_factories


@pytest.mark.unit
class TestPersonaModel:
    """Test cases for the Persona model."""
    
    def test_persona_creation_with_required_fields(self, db_session):
        """Test persona creation with only required fields."""
        from models.persona import Persona
        
        persona = Persona(
            dni="12345678",
            nombre="Juan",
            apellido="Pérez",
            genero=GeneroEnum.M
        )
        
        db_session.add(persona)
        db_session.commit()
        
        assert persona.id is not None
        assert persona.dni == "12345678"
        assert persona.nombre == "Juan"
        assert persona.apellido == "Pérez"
        assert persona.genero == GeneroEnum.M
    
    def test_persona_creation_with_all_fields(self, db_session):
        """Test persona creation with all fields."""
        from models.persona import Persona
        
        persona = Persona(
            dni="87654321",
            nombre="María",
            apellido="González",
            telefono="+54911234567",
            genero=GeneroEnum.F,
            direccion="Av. Corrientes 1234",
            email="maria.gonzalez@email.com"
        )
        
        db_session.add(persona)
        db_session.commit()
        
        assert persona.telefono == "+54911234567"
        assert persona.direccion == "Av. Corrientes 1234"
        assert persona.email == "maria.gonzalez@email.com"
    
    def test_persona_dni_unique_constraint(self, db_session):
        """Test that DNI must be unique."""
        from models.persona import Persona
        
        # Create first persona
        persona1 = Persona(
            dni="11111111",
            nombre="Pedro",
            apellido="López",
            genero=GeneroEnum.M
        )
        db_session.add(persona1)
        db_session.commit()
        
        # Try to create another persona with same DNI
        persona2 = Persona(
            dni="11111111",  # Same DNI
            nombre="Ana",
            apellido="Martín",
            genero=GeneroEnum.F
        )
        db_session.add(persona2)
        
        with pytest.raises(IntegrityError):
            db_session.commit()
    
    def test_persona_dni_not_null(self, db_session):
        """Test that DNI cannot be null."""
        from models.persona import Persona
        
        persona = Persona(
            # dni=None,  # Missing DNI
            nombre="Sin",
            apellido="DNI",
            genero=GeneroEnum.INDETERMINADO
        )
        
        db_session.add(persona)
        
        with pytest.raises(IntegrityError):
            db_session.commit()
    
    def test_persona_nombre_not_null(self, db_session):
        """Test that nombre cannot be null."""
        from models.persona import Persona
        
        persona = Persona(
            dni="22222222",
            # nombre=None,  # Missing nombre
            apellido="Sin Nombre",
            genero=GeneroEnum.INDETERMINADO
        )
        
        db_session.add(persona)
        
        with pytest.raises(IntegrityError):
            db_session.commit()
    
    def test_persona_apellido_not_null(self, db_session):
        """Test that apellido cannot be null."""
        from models.persona import Persona
        
        persona = Persona(
            dni="33333333",
            nombre="Sin Apellido",
            # apellido=None,  # Missing apellido
            genero=GeneroEnum.INDETERMINADO
        )
        
        db_session.add(persona)
        
        with pytest.raises(IntegrityError):
            db_session.commit()
    
    def test_persona_genero_enum_validation(self, db_session):
        """Test that genero accepts only valid enum values."""
        from models.persona import Persona
        
        # Valid genero values
        for genero in [GeneroEnum.M, GeneroEnum.F, GeneroEnum.INDETERMINADO]:
            persona = Persona(
                dni=f"444444{genero.value}",
                nombre="Test",
                apellido="User",
                genero=genero
            )
            db_session.add(persona)
            db_session.commit()
            assert persona.genero == genero
            
            # Clear session for next iteration
            db_session.expunge(persona)
    
    def test_persona_relationships(self, db_session):
        """Test persona relationships are properly configured."""
        set_session_for_factories(db_session)
        
        persona = PersonaFactory()
        db_session.commit()
        
        # Test that relationships are properly initialized
        assert hasattr(persona, 'usuario')
        assert hasattr(persona, 'responsable')
        assert hasattr(persona, 'ventas')
        assert hasattr(persona, 'empleado')
    
    def test_persona_factory(self, db_session):
        """Test that PersonaFactory creates valid personas."""
        set_session_for_factories(db_session)
        
        persona = PersonaFactory()
        db_session.commit()
        
        assert persona.id is not None
        assert len(persona.dni) == 8
        assert persona.dni.isdigit()
        assert persona.nombre is not None
        assert persona.apellido is not None
        assert persona.genero in [GeneroEnum.M, GeneroEnum.F, GeneroEnum.INDETERMINADO]
    
    def test_persona_str_representation(self, db_session):
        """Test string representation of persona (if implemented)."""
        from models.persona import Persona
        
        persona = Persona(
            dni="55555555",
            nombre="Carlos",
            apellido="Rodríguez",
            genero=GeneroEnum.M
        )
        
        # This test assumes a __str__ method exists
        # If not implemented, this will just test the default representation
        str_repr = str(persona)
        assert isinstance(str_repr, str)
        assert len(str_repr) > 0
    
    def test_persona_email_format(self, db_session):
        """Test that email field accepts various formats."""
        from models.persona import Persona
        
        valid_emails = [
            "user@example.com",
            "test.email@domain.org",
            "user+tag@subdomain.example.com",
            None  # Email is optional
        ]
        
        for i, email in enumerate(valid_emails):
            persona = Persona(
                dni=f"6666666{i}",
                nombre="Test",
                apellido="Email",
                genero=GeneroEnum.INDETERMINADO,
                email=email
            )
            db_session.add(persona)
            db_session.commit()
            assert persona.email == email
            
            # Clear session for next iteration
            db_session.expunge(persona)