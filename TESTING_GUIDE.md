# Testing Guide for Veterinary Backend

This document provides comprehensive examples and best practices for testing the veterinary backend application.

## Table of Contents

1. [Test Structure](#test-structure)
2. [Test Categories](#test-categories)
3. [Running Tests](#running-tests)
4. [Test Examples](#test-examples)
5. [Best Practices](#best-practices)
6. [Common Patterns](#common-patterns)

## Test Structure

```
tests/
├── __init__.py                    # Makes tests a Python package
├── conftest.py                   # Global test configuration and fixtures
├── factories.py                  # Test data factories using Factory Boy
├── unit/                        # Unit tests for individual components
│   ├── test_animal_model.py     # Tests for Animal model
│   └── test_persona_model.py    # Tests for Persona model
├── integration/                 # Integration tests for component interactions
│   └── test_database_operations.py
├── api/                        # API endpoint tests
│   └── test_main_endpoints.py
└── fixtures/                   # Reusable test fixtures
    └── common_fixtures.py
```

## Test Categories

### Unit Tests (@pytest.mark.unit)
- Test individual model validation
- Test model relationships
- Test business logic in isolation
- Fast execution, no external dependencies

### Integration Tests (@pytest.mark.integration)
- Test database operations
- Test model interactions
- Test transaction handling
- Test complex queries

### API Tests (@pytest.mark.api)
- Test HTTP endpoints
- Test request/response validation
- Test status codes
- Test error handling

## Running Tests

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest
```

### Run Specific Test Categories
```bash
# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Run only API tests
pytest -m api
```

### Run Tests with Coverage
```bash
pytest --cov=. --cov-report=html
```

### Run Specific Test Files
```bash
# Run animal model tests
pytest tests/unit/test_animal_model.py

# Run database integration tests
pytest tests/integration/test_database_operations.py
```

### Run Tests in Verbose Mode
```bash
pytest -v
```

## Test Examples

### 1. Basic Model Test

```python
@pytest.mark.unit
def test_animal_creation(db_session):
    """Test basic animal creation."""
    from models.animal import Animal
    
    animal = Animal(
        nombre="Rex",
        especie="Perro",
        sexo=GeneroEnum.M,
        alergias="Ninguna",
        responsable_id=1
    )
    
    db_session.add(animal)
    db_session.commit()
    
    assert animal.id is not None
    assert animal.nombre == "Rex"
```

### 2. Relationship Test

```python
@pytest.mark.unit
def test_animal_responsable_relationship(db_session):
    """Test animal-responsable relationship."""
    set_session_for_factories(db_session)
    
    animal = AnimalFactory()
    db_session.commit()
    
    assert animal.responsable is not None
    assert animal in animal.responsable.animales
```

### 3. Validation Test

```python
@pytest.mark.unit
def test_animal_requires_responsable(db_session):
    """Test that animal requires a responsable."""
    from models.animal import Animal
    
    animal = Animal(
        nombre="Orphan",
        especie="Perro",
        sexo=GeneroEnum.M,
        alergias="Ninguna"
        # No responsable_id
    )
    
    db_session.add(animal)
    
    with pytest.raises(IntegrityError):
        db_session.commit()
```

### 4. API Endpoint Test

```python
@pytest.mark.api
def test_get_root_endpoint(client):
    """Test the root endpoint."""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Hola desde Docker y FastAPI! cambioooos"}
```

### 5. Factory Usage

```python
def test_using_factories(db_session):
    """Example of using factories for test data."""
    set_session_for_factories(db_session)
    
    # Create multiple animals quickly
    animals = [AnimalFactory() for _ in range(5)]
    db_session.commit()
    
    assert len(animals) == 5
    for animal in animals:
        assert animal.id is not None
```

### 6. Fixture Usage

```python
def test_using_fixtures(sample_animal):
    """Example of using predefined fixtures."""
    assert sample_animal.nombre == "Milo"
    assert sample_animal.especie == "Perro"
    assert sample_animal.responsable is not None
```

## Best Practices

### 1. Test Naming Convention
- Use descriptive names: `test_animal_creation_with_valid_data`
- Start with `test_`
- Describe what is being tested and expected outcome

### 2. Test Structure (AAA Pattern)
```python
def test_example():
    # Arrange - Set up test data
    animal = AnimalFactory()
    
    # Act - Perform the action being tested
    animal.nombre = "New Name"
    db_session.commit()
    
    # Assert - Verify the results
    assert animal.nombre == "New Name"
```

### 3. Use Factories for Test Data
```python
# Good - Using factories
animal = AnimalFactory(especie="Gato")

# Avoid - Manual creation for complex objects
animal = Animal(
    nombre="Test",
    especie="Gato",
    # ... many fields
)
```

### 4. Test One Thing at a Time
```python
# Good - Tests one specific behavior
def test_animal_soft_delete():
    animal.borrado = True
    assert animal.borrado is True

# Avoid - Testing multiple behaviors
def test_animal_operations():
    # Creates, updates, deletes all in one test
```

### 5. Use Appropriate Markers
```python
@pytest.mark.unit      # For unit tests
@pytest.mark.integration  # For integration tests
@pytest.mark.api       # For API tests
@pytest.mark.slow      # For slow tests
```

### 6. Handle Database State
```python
def test_with_rollback(db_session):
    # Test changes are automatically rolled back
    # due to session fixture configuration
    pass
```

## Common Patterns

### 1. Testing Exceptions
```python
def test_invalid_data_raises_exception(db_session):
    with pytest.raises(IntegrityError):
        # Code that should raise IntegrityError
        pass
```

### 2. Testing Optional Parameters
```python
@pytest.mark.parametrize("especie", ["Perro", "Gato", "Conejo"])
def test_animal_especies(db_session, especie):
    animal = AnimalFactory(especie=especie)
    assert animal.especie == especie
```

### 3. Testing Timestamps
```python
def test_creation_timestamp(db_session):
    before = datetime.now()
    animal = AnimalFactory()
    db_session.commit()
    after = datetime.now()
    
    assert before <= animal.fecha_creacion <= after
```

### 4. Testing Complex Queries
```python
def test_complex_query(db_session):
    # Create test data
    animals = [
        AnimalFactory(especie="Perro"),
        AnimalFactory(especie="Gato"),
        AnimalFactory(especie="Perro")
    ]
    db_session.commit()
    
    # Test query
    dogs = db_session.query(Animal).filter(
        Animal.especie == "Perro"
    ).all()
    
    assert len(dogs) == 2
```

### 5. Testing API Responses
```python
def test_api_response_format(client):
    response = client.get("/api/animals/1")
    
    assert response.status_code == 200
    data = response.json()
    
    # Test response structure
    required_fields = ["id", "nombre", "especie", "sexo"]
    for field in required_fields:
        assert field in data
```

## Configuration Files

### pytest.ini
```ini
[tool:pytest]
minversion = 6.0
testpaths = tests
python_files = test_*.py
markers =
    unit: Unit tests
    integration: Integration tests
    api: API endpoint tests
    slow: Slow running tests
```

### Test Database Configuration
The test suite uses SQLite by default for fast, isolated testing. Each test gets a clean database state through the session fixtures.

## Continuous Integration

For CI/CD pipelines, add this command to run tests:

```bash
pytest --cov=. --cov-report=xml --junitxml=test-results.xml
```

This generates coverage reports and test results in formats that CI systems can parse.

## Debugging Tests

### Run with Debugging
```bash
pytest -s -vv  # Show print statements and verbose output
pytest --pdb   # Drop into debugger on failures
```

### Show Coverage Gaps
```bash
pytest --cov=. --cov-report=term-missing
```

This shows exactly which lines are not covered by tests.