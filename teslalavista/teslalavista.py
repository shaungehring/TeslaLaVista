from teslalavista.classes.api import TeslaAPI
from teslalavista.classes.vehicles import VehicleCollection, Vehicle

class TeslaLaVista(object):

    def __init__(self, username: str = None, password: str = None):
        self.api = TeslaAPI()

        self.vehicle_collection = None

        if username and password:
            self.__connect_and_refresh(username=username, password=password)

    def connect(self, username: str = None, password: str = None) -> None:

        if username and password:
            self.__connect_and_refresh(username=username, password=password)

    def __connect_and_refresh(self, username: str = None, password: str = None) -> None:

        self.api.refresh_access_token(
            username=username,
            password=password
        )

        self.__refresh_data()

    def __refresh_data(self) -> None:
        vc = VehicleCollection()

        vehicles_data = self.api.vehicles()

        for car in vehicles_data:
            vehicle = Vehicle(api_object=self.api, vehicle_json=car)

            vehicle.update()

            vc.add_vehicle(vehicle=vehicle)

        self.vehicle_collection = vc


    def vehicles(self) -> VehicleCollection:

        return self.vehicle_collection

    def vehicle(self, id: int = None, name: str = None) -> Vehicle:

        if id:
            return self.vehicle_collection.get_vehicle_by_id(id=id)
        elif name:
            return self.vehicle_collection.get_vehicle_by_name(name=name)
        else:
            return None