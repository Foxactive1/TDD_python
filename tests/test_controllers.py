from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "price": 1000})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_update_product_not_found():
    response = client.patch("/products/2", json={"price": 1500, "updated_at": "2024-07-13T00:00:00Z"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_get_products():
    response = client.get("/products/", params={"price_min": 5000, "price_max": 8000})
    assert response.status_code == 200
    assert len(response.json()) > 0
