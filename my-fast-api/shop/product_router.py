from fastapi import APIRouter , HTTPException , status
from models import ProductResponse, ProductCreate, ProductPatch
from service import ProductService
from repository import ProductRepository , ProductException
from starlette.exceptions import HTTPException

router = APIRouter(prefix="/products", tags=["products"])
product_service = ProductService(product_repository= ProductRepository())

@router.post("/" , response_model= ProductResponse , status_code=status.HTTP_201_CREATED)

def create_product(prod: ProductCreate) -> ProductResponse:
    try:
        return product_service.create_product(prod)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.get("/id/{prod_id}")

def get_product_by_id(prod_id:int) -> ProductResponse:
    try:
        return product_service.get_by_id(prod_id)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.get("/by-name/{name}")

def get_product_by_name(name:str) -> ProductResponse:
    try:
        return product_service.get_by_product_name(name)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{prod_id}")

def update_product(prod_id:int, prod: ProductCreate) -> ProductResponse:
    try:
        return product_service.update_product(prod_id, prod)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.patch("/{prod_id}")

def patch_product(prod_id:int, product_patch: ProductPatch) -> ProductResponse:
    try:
        return product_service.patch_product(prod_id, product_patch)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{prod_id}")

def delete_product(prod_id:int):
    try:
        return product_service.delete_product(prod_id)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))