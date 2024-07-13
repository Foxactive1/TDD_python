from app.models.product import Product
from datetime import datetime

def create_product_usecase(product: Product):
    # Logic to save the product in the database
    product.created_at = datetime.utcnow()
    product.updated_at = datetime.utcnow()
    # Simulate save
    return product

def update_product_usecase(product_id: str, product_update: ProductUpdate):
    # Logic to update the product in the database
    # Simulate find and update
    product = find_product_by_id(product_id)
    if not product:
        return None
    if product_update.name:
        product.name = product_update.name
    if product_update.price:
        product.price = product_update.price
    product.updated_at = product_update.updated_at
    # Simulate save
    return product

def get_products_usecase(price_min: float, price_max: float):
    # Logic to filter products by price range
    # Simulate query
    products = [
        Product(id="1", name="Product 1", price=6000, created_at=datetime.utcnow(), updated_at=datetime.utcnow()),
        Product(id="2", name="Product 2", price=7000, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    ]
    return [p for p in products if price_min < p.price < price_max]

def find_product_by_id(product_id: str) -> Product:
    # Simulate database search
    if product_id == "1":
        return Product(id="1", name="Product 1", price=6000, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    return None
