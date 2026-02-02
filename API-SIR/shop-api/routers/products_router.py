
from fastapi import APIRouter
from starlette import status
from starlette.exceptions import HTTPException

from models import ProductResponse, ProductCreate
from services import ProductService, ProductServiceException

router = APIRouter(prefix="/products", tags=["products"])

product_service = ProductService()

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(prod : ProductCreate):
    try:
        product_service.create_product(prod)
    except ProductServiceException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    