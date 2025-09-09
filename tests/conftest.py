"""
Test configuration and shared fixtures.

This module provides the basic configuration and fixtures needed for testing
the veterinary backend application.
"""

import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from unittest.mock import patch

# Test database URL - use in-memory SQLite for testing
TEST_DATABASE_URL = "sqlite:///./test.db"

def get_test_database_url():
    """Get the test database URL, defaulting to SQLite for testing."""
    return os.getenv("TEST_DATABASE_URL", TEST_DATABASE_URL)

@pytest.fixture(scope="session")
def test_engine():
    """Create a test database engine."""
    # Create engine for test database
    engine = create_engine(
        get_test_database_url(),
        connect_args={"check_same_thread": False}  # For SQLite
    )
    
    # Import models to ensure tables are created
    with patch.dict(os.environ, {'DATABASE_URL': get_test_database_url()}):
        from config.database import Base
        Base.metadata.create_all(bind=engine)
    
    yield engine
    
    # Cleanup
    if os.path.exists("./test.db"):
        os.remove("./test.db")

@pytest.fixture
def db_session(test_engine):
    """Create a database session for testing."""
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=test_engine
    )
    
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()  # Rollback any changes
        session.close()

@pytest.fixture
def client():
    """Create a test client."""
    # Set environment variable for testing
    with patch.dict(os.environ, {'DATABASE_URL': get_test_database_url()}):
        from main import app
        
        with TestClient(app) as test_client:
            yield test_client

@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {
        'DATABASE_URL': get_test_database_url(),
        'SECRET_KEY': 'test-secret-key',
        'ENVIRONMENT': 'testing'
    }):
        yield