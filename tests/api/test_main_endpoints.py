"""
API endpoint tests using FastAPI TestClient.

These tests demonstrate how to test FastAPI endpoints,
including request/response validation, status codes, and error handling.
"""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.mark.api
class TestMainEndpoints:
    """Test the main application endpoints."""
    
    def test_root_endpoint(self, client):
        """Test the root endpoint returns correct response."""
        response = client.get("/")
        
        assert response.status_code == 200
        assert response.json() == {"mensaje": "¡Hola desde Docker y FastAPI! cambioooos"}
    
    def test_url_endpoint(self, client):
        """Test the /url endpoint."""
        response = client.get("/url")
        
        assert response.status_code == 200
        assert response.json() == {"mensaje": "urljson"}
    
    def test_nonexistent_endpoint(self, client):
        """Test that non-existent endpoints return 404."""
        response = client.get("/nonexistent")
        
        assert response.status_code == 404
    
    def test_method_not_allowed(self, client):
        """Test that wrong HTTP methods return 405."""
        # Try POST on GET-only endpoint
        response = client.post("/")
        
        assert response.status_code == 405


@pytest.mark.api 
class TestAPIHealthAndMeta:
    """Test API health and metadata endpoints."""
    
    def test_app_instance(self):
        """Test that the FastAPI app instance is properly configured."""
        assert app is not None
        assert hasattr(app, "routes")
        assert len(app.routes) > 0
    
    def test_client_headers(self, client):
        """Test that the test client properly handles headers."""
        response = client.get("/", headers={"User-Agent": "test-client"})
        
        assert response.status_code == 200
    
    def test_json_content_type(self, client):
        """Test that responses have correct content type."""
        response = client.get("/")
        
        assert response.status_code == 200
        assert "application/json" in response.headers.get("content-type", "")


# Example of how to test future API endpoints for the veterinary system
@pytest.mark.api
class TestFutureVeterinaryEndpoints:
    """Examples of how to test veterinary-specific endpoints when they're implemented."""
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_list_animals_endpoint(self, client):
        """Example test for a future animals listing endpoint."""
        response = client.get("/api/animals")
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_create_animal_endpoint(self, client):
        """Example test for a future animal creation endpoint."""
        animal_data = {
            "nombre": "Rex",
            "especie": "Perro",
            "sexo": "M",
            "alergias": "Ninguna",
            "responsable_id": 1
        }
        
        response = client.post("/api/animals", json=animal_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["nombre"] == "Rex"
        assert data["especie"] == "Perro"
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_get_animal_by_id(self, client):
        """Example test for getting a specific animal."""
        animal_id = 1
        response = client.get(f"/api/animals/{animal_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == animal_id
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_get_animal_not_found(self, client):
        """Example test for handling non-existent animals."""
        response = client.get("/api/animals/99999")
        
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_update_animal_endpoint(self, client):
        """Example test for updating an animal."""
        animal_id = 1
        update_data = {
            "nombre": "Rex Updated",
            "peso": "15kg"
        }
        
        response = client.put(f"/api/animals/{animal_id}", json=update_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["nombre"] == "Rex Updated"
        assert data["peso"] == "15kg"
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_delete_animal_endpoint(self, client):
        """Example test for soft-deleting an animal."""
        animal_id = 1
        response = client.delete(f"/api/animals/{animal_id}")
        
        assert response.status_code == 204
        
        # Verify animal is soft-deleted
        get_response = client.get(f"/api/animals/{animal_id}")
        assert get_response.status_code == 404
    
    @pytest.mark.skip(reason="Endpoint not implemented yet") 
    def test_list_responsables_endpoint(self, client):
        """Example test for listing responsables."""
        response = client.get("/api/responsables")
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_create_responsable_with_persona(self, client):
        """Example test for creating responsable with persona data."""
        responsable_data = {
            "persona": {
                "dni": "12345678",
                "nombre": "Juan",
                "apellido": "Pérez",
                "genero": "M",
                "telefono": "1234567890",
                "email": "juan@email.com"
            },
            "aceptaRecordatorios": True
        }
        
        response = client.post("/api/responsables", json=responsable_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["persona"]["dni"] == "12345678"
        assert data["aceptaRecordatorios"] is True
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_validation_error_handling(self, client):
        """Example test for API validation error handling."""
        invalid_animal_data = {
            "nombre": "",  # Empty name should fail validation
            "especie": "InvalidSpecies",
            "sexo": "X"  # Invalid gender
        }
        
        response = client.post("/api/animals", json=invalid_animal_data)
        
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_pagination(self, client):
        """Example test for paginated endpoints."""
        response = client.get("/api/animals?page=1&size=10")
        
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "total" in data
        assert "page" in data
        assert "size" in data
        assert len(data["items"]) <= 10
    
    @pytest.mark.skip(reason="Endpoint not implemented yet")
    def test_filtering_and_search(self, client):
        """Example test for filtering animals."""
        response = client.get("/api/animals?especie=Perro&sexo=M")
        
        assert response.status_code == 200
        data = response.json()
        for animal in data:
            assert animal["especie"] == "Perro"
            assert animal["sexo"] == "M"


@pytest.mark.api
class TestAPIErrorHandling:
    """Test API error handling scenarios."""
    
    def test_invalid_json_request(self, client):
        """Test handling of invalid JSON in request body."""
        response = client.post(
            "/url",  # Using existing endpoint for testing
            content="invalid json{",
            headers={"Content-Type": "application/json"}
        )
        
        # Should handle invalid JSON gracefully
        # Status code depends on FastAPI's default handling
        assert response.status_code in [400, 405, 422]
    
    def test_large_request_body(self, client):
        """Test handling of large request bodies."""
        large_data = {"data": "x" * 10000}  # 10KB of data
        
        response = client.post("/url", json=large_data)
        
        # Should handle large requests (status depends on implementation)
        assert response.status_code in [200, 405, 413, 422]