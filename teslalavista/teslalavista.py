from teslalavista.classes.api import TeslaAPI
from teslalavista.classes.vehicles import VehicleCollection, Vehicle

class TeslaLaVista(object):

    def __init__(self, username: str = None, password: str = None):
        """Initialize the client.

        You have the option to initialize using the User/Pass

        Args:
            username (str): Username for Tesla Account
            password (str): Password  for Tesla Account
        """
        self.api = TeslaAPI()

        self.vehicle_collection = None

        if username and password:
            self.__connect_and_refresh(username=username, password=password)

    def connect(self, username: str = None, password: str = None) -> None:

        """Connect using User/Pass

        Args:
            username (str): Username for Tesla Account
            password (str): Password  for Tesla Account
        """
        if username and password:
            self.__connect_and_refresh(username=username, password=password)

    def __connect_and_refresh(self, username: str = None, password: str = None) -> None:

        """Take the User/Pass and request Vehicle Data

        Args:
            username (str): Username for Tesla Account
            password (str): Password  for Tesla Account
        """
        self.api.refresh_access_token(
            username=username,
            password=password
        )

        self.__refresh_data()

    def __refresh_data(self) -> None:

        """Refesh the data from the API

        Get the most recent status on all vehicles from the API
        """
        vc = VehicleCollection()

        vehicles_data = self.api.vehicles()

        for car in vehicles_data:
            vehicle = Vehicle(api_object=self.api, vehicle_json=car)

            vehicle.update()

            vc.add_vehicle(vehicle=vehicle)

        self.vehicle_collection = vc


    def vehicles(self) -> VehicleCollection:

        """Get the Vehicle Collection Object

        Gets the Collection object for vehicles
        """

        return self.vehicle_collection

    def vehicle(self, id: int = None, name: str = None) -> Vehicle:

        """Get a Vehicle by it's ID or Name

        Request a specific Vehicle using it's ID or it's Name. If neither are supplied then you get None back

        Args:
            id (int): (Optional) The ID of the Vehicle
            name (str): (Optional) The name of the Vehicle
        """
        if id:
            return self.vehicle_collection.get_vehicle_by_id(id=id)
        elif name:
            return self.vehicle_collection.get_vehicle_by_name(name=name)
        else:
            return None