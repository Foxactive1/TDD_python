from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.usecases.product_usecase import create_product_usecase, update_product_usecase, get_products_usecase

router = APIRouter()

@router.post("/products/")
def create_product(product: ProductCreate):
    try:
        result = create_product_usecase(product)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/products/{product_id}")
def update_product(product_id: str, product_update: ProductUpdate):
    try:
        result = update_product_usecase(product_id, product_update)
        if not result:
            raise HTTPException(status_code=404, detail="Product not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/products/")
def get_products(price_min: float, price_max: float):
    return get_products_usecase(price_min, price_max)
