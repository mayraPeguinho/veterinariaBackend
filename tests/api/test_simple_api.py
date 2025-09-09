"""
Simple API test example that works with current versions.

This demonstrates a basic test approach without complex TestClient setup.
"""

import pytest
import os
from unittest.mock import patch


@pytest.mark.api
def test_app_import():
    """Test that the FastAPI app can be imported successfully."""
    with patch.dict(os.environ, {'DATABASE_URL': 'sqlite:///test.db'}):
        from main import app
        assert app is not None
        assert hasattr(app, 'routes')


@pytest.mark.api 
def test_basic_route_definition():
    """Test that basic routes are defined."""
    with patch.dict(os.environ, {'DATABASE_URL': 'sqlite:///test.db'}):
        from main import app
        
        # Get route paths
        route_paths = [route.path for route in app.routes if hasattr(route, 'path')]
        
        assert "/" in route_paths
        assert "/url" in route_paths


@pytest.mark.api
def test_route_functions():
    """Test route functions directly."""
    with patch.dict(os.environ, {'DATABASE_URL': 'sqlite:///test.db'}):
        from main import read_root, read_url
        
        # Test root function
        result = read_root()
        assert result == {"mensaje": "¡Hola desde Docker y FastAPI! cambioooos"}
        
        # Test url function  
        result = read_url()
        assert result == {"mensaje": "urljson"}