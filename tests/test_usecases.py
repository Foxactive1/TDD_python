from app.usecases.product_usecase import create_product_usecase, update_product_usecase, get_products_usecase
from app.schemas.product_schema import ProductCreate, ProductUpdate
from datetime import datetime

def test_create_product_usecase():
    product = ProductCreate(name="New Product", price=2000)
    result = create_product_usecase(product)
    assert result.name == "New Product"
    assert result.price == 2000

def test_update_product_usecase_not_found():
    product_update = ProductUpdate(price=1500, updated_at=datetime.utcnow())
    result = update_product_usecase("2", product_update)
    assert result is None

def test_get_products_usecase():
    result = get_products_usecase(5000, 8000)
    assert len(result) > 0
