from data_access.database import DatabaseAccess

class CarService:
    def __init__(self):
        self.database_access = DatabaseAccess()

    def add_new_car(self, car_RegistrationNumber, car_Make, car_Year, car_Color):
        self.database_access.add_car(car_RegistrationNumber, car_Make, car_Year, car_Color)

    def get_all_cars(self):
        return self.database_access.get_all_cars()
