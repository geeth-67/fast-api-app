from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel , Field


class CarTypes(str , Enum):       #enum can more clear our code,
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    VAN = "van"
    LORRY = "lorry"

class FuelTypes(Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    EV = "ev"

class CarBase(BaseModel):
    make : str = Field(...,min_length=1 , max_length=60 , description="Car Manufacturer")
    model : str = Field(...,min_length=1 , max_length=60 , description="Car Model")
    year : int = Field(...,ge=2000 , description="Manufacturer year")
    car_type : CarTypes = Field(description="Type of car")
    fuel_type : FuelTypes = Field(description="Fuel type")
    rate_per_km : float = Field(ge=0 , le=1000 , description="Rate per kilo meter")
    mileage : float = Field(ge=0 , le=0 , description="Mileage of the vehicle")
    licence_plate : str = Field(description="Licence Plate number")

class CarResponse(CarBase):
    id :int
    created_at : str
    updated_at : str

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    pass

class CarPatch(BaseModel):
    make: Optional[str] = Field(None, min_length=1, max_length=60, description="Car Manufacturer")
    model: Optional[str] = Field(None, min_length=1, max_length=60, description="Car Model")
    year: Optional[int] = Field(None, ge=2000, description="Manufacturer year")
    car_type: Optional[CarTypes] = Field(None,description="Type of car")
    fuel_type: Optional[FuelTypes] = Field(None,description="Fuel type")
    rate_per_km: Optional[float] = Field(None,ge=0, le=1000, description="Rate per kilo meter")
    mileage: Optional[float] = Field(None,ge=0, le=0, description="Mileage of the vehicle")
    licence_plate: Optional[str] = Field(None,description="Licence Plate number")
