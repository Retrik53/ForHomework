import json
import pickle


class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def info(self):
        print(f"Name: {self.name}, Capacity: {self.capacity}, Location: {self.location}")

    def update_location(self, new_location):
        self.location = new_location

    class StadiumAdapter:
        def __init__(self, stadium):
            self.stadium = stadium

        def to_dict(self):
            return {
                'name': self.stadium.name,
                'capacity': self.stadium.capacity,
                'location': self.stadium.location
            }

    def to_json(self):
        adapter = Stadium.StadiumAdapter(self)
        return json.dumps(adapter.to_dict())

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        stadium = Stadium(data['name'], data['capacity'], data['location'])
        return stadium

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickled_data):
        return pickle.loads(pickled_data)

stadium = Stadium("Camp Nou", 99354, "Barcelona, Spain")

stadium.info()

stadium.update_location("Madrid, Spain")
stadium.info()

json_stadium = stadium.to_json()
print(json_stadium)

new_stadium = Stadium.from_json(json_stadium)
new_stadium.info()

pickled_stadium = stadium.to_pickle()

unpickled_stadium = Stadium.from_pickle(pickled_stadium)
unpickled_stadium.info()