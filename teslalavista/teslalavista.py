from teslalavista.classes.api import TeslaAPI
from teslalavista.classes.vehicles import VehicleCollection, Vehicle, ONLINE_STATE

class TeslaLaVista(object):

    def __init__(self, username=None, password=None):
        self.api = TeslaAPI()

        self.vehicle_collection = None

        if username and password:
            self.__connect_and_refresh(username=username, password=password)

    def connect(self, username=None, password=None):

        if username and password:
            self.__connect_and_refresh(username=username, password=password)

    def __connect_and_refresh(self, username=None, password=None):

        self.api.refresh_access_token(
            username=username,
            password=password
        )

        self.__refresh_data()

    def __refresh_data(self):
        vc = VehicleCollection()

        vehicles_data = self.api.vehicles().json()["response"]

        for car in vehicles_data:
            vehicle = Vehicle(api_object=self.api, vehicle_json=car)

            vehicle.update()

            vc.add_vehicle(vehicle=vehicle)

        self.vehicle_collection = vc


    def vehicles(self):

        return self.vehicle_collection

    def vehicle(self, id=None, name=None):

        if id:
            return self.vehicle_collection.get_vehicle_by_id(id=id)
        elif name:
            return self.vehicle_collection.get_vehicle_by_name(name=name)
        else:
            return None