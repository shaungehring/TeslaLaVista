import unittest
import pytest
import os

from teslalavista.teslalavista import TeslaLaVista

class TestAPI(unittest.TestCase):
    tlv = TeslaLaVista(
        username=os.getenv('username', ''),
        password=os.getenv('password', '')
        )

    def test_vehicle_collection(self):
        vehicles = self.tlv.vehicles()

        for vehicle in vehicles.get_vehicles():
            print(vehicle.name)