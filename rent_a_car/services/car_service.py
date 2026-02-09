from dataclasses import dataclass
from rent_a_car.models.car_models import CarResponse, CarCreate, CarUpdate, CarPatch
from rent_a_car.repositories.car_repository import CarRepository


@dataclass
class CarService:

    car_repo : CarRepository

    def create_car(self , car : CarCreate):
        return self.car_repo.create_car(car)

    def update_car(self ,car_id : int , car : CarUpdate):
        return self.car_repo.update_car(car_id , car)

    def patch_car(self , car_id : int , car : CarPatch):
        return self.car_repo.patch_car(car_id , car)

    def get_by_id(self , car_id : int):
        return self.car_repo.get_by_id(car_id)

    def list_all_cars(self , offset:int, limit:int):
        return self.car_repo.list_all_cars()

    def delete_car(self , car_id : int ):
        return self.car_repo.delete_car(car_id)