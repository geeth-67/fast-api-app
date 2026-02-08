from datetime import datetime
from typing import Dict, Optional , List
from rent_a_car.models.car_models import CarResponse, CarBase, CarUpdate, CarPatch, CarCreate


class CarException(Exception):
    pass

class CarRepository:

    def __init__(self):
        self.cars: Dict[int, CarResponse] = {}
        self.count : int = 1

    def create_car(self , car : CarCreate):
        car_obj = CarResponse(
            id= self.count,
            make= car.make,
            model=car.model,
            year= car.year,
            car_type= car.car_type,
            fuel_type= car.fuel_type,
            rate_per_km= car.rate_per_km,
            mileage= car.mileage,
            licence_plate= car.licence_plate,
            created_at= datetime.now().isoformat(),
            updated_at= datetime.now().isoformat()
        )
        self.cars[self.count] = car_obj
        self.count += 1
        return car_obj

    def update_car(self, car_id ,car: CarUpdate):

        if car_id not in self.cars.keys():
            raise CarException('Car id not found !')

        existing_car = self.cars[car_id]

        self.cars[car_id] = CarResponse(
            id=car_id,
            make=car.make,
            model=car.model,
            year=car.year,
            car_type=car.car_type,
            fuel_type=car.fuel_type,
            rate_per_km=car.rate_per_km,
            mileage=car.mileage,
            licence_plate=car.licence_plate,
            created_at=existing_car.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )

        update = self.cars[car_id]
        return {"message": "successfully update Car", "car": update}

    def get_by_id(self , car_id : int)->Optional[CarResponse]:

        car = self.cars.get(car_id)
        if car is None:
            raise CarException("car id not found!")

        return car

    def list_all_cars(self , offset= int , limit= int)->List[CarResponse]:

        cars = [car for car in self.cars.values()]
        return cars[offset: offset + limit]

    def patch_car(self , car_id : int , car : CarPatch)->None:

        if car_id not in self.cars.keys():
            raise CarException("Car id not found!")

        existing_car = self.cars[car_id]
        updated_data = car.model_dump(exclude_unset=True)
        update_car = existing_car.model_copy(update=updated_data)
        self.cars[car_id] = update_car

    def delete_car(self , car_id : int):

        if car_id not in self.cars.keys():
            raise CarException("car id not existing")

        del_car = self.cars.pop(car_id)
        return f"successfully deleted car , car is : {del_car}"