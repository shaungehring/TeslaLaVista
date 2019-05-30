import unittest
import pytest
import os

from teslalavista.teslalavista import TeslaLaVista

class TestAPI(unittest.TestCase):
    tlv = TeslaLaVista(
        username=os.getenv('username', ''),
        password=os.getenv('password', '')
        )

    # def test_vehicle_collection(self):
    #     vehicles = self.tlv.vehicles()
    #
    #     for vehicle in vehicles.get_vehicles():
    #         print(vehicle.name)

    # def test_vehicle_horn(self):
    #     vehicles = self.tlv.vehicles()
    #
    #     my_car = vehicles.get_vehicle_by_name(name="Black Beauty")
    #
    #     my_car.honk_horn()