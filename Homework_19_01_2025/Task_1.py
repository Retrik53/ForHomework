import json
import pickle


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def update_year(self, new_year):
        self.year = new_year

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        car = Car(data['make'], data['model'], data['year'])
        return car

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickled_data):
        return pickle.loads(pickled_data)

car = Car("Toyota", "Corolla", 2020)

car.info()

car.update_year(2021)
car.info()

json_car = car.to_json()
print(json_car)

new_car = Car.from_json(json_car)
new_car.info()

pickled_car = car.to_pickle()

unpickled_car = Car.from_pickle(pickled_car)
unpickled_car.info()