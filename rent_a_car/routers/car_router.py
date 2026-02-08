from fastapi import APIRouter , HTTPException , status
from rent_a_car.models.car_models import CarCreate, CarUpdate, CarPatch
from rent_a_car.repositories.car_repository import CarRepository, CarResponse, CarException
from rent_a_car.services.car_service import CarService

router = APIRouter(prefix="/cars" , tags=["cars"])
car_service = CarService(car_repo= CarRepository())

@router.post("/" , response_model=CarResponse , status_code=status.HTTP_201_CREATED)

def create_car( car : CarCreate)->CarResponse:
    try:
        return car_service.create_car(car)
    except CarException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

@router.get("/id/{car_id}")

def get_by_car_id(car_id:int) -> CarResponse:
    try:
        return car_service.get_by_id(car_id)
    except CarException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{prod_id}")

def update_car(car_id:int, car: CarUpdate) -> CarResponse:
    try:
        return car_service.update_car(car_id,car)
    except CarException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.patch("/{prod_id}")

def patch_car(car_id:int, car_patch: CarPatch) -> CarResponse:
    try:
        return car_service.patch_car(car_id, car_patch)
    except CarException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{prod_id}")

def delete_car(car_id:int):
    try:
        return car_service.delete_car(car_id)
    except CarException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))