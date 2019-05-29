import unittest
import pytest
import os

from teslalavista.classes.api import TeslaAPI

class TestAPI(unittest.TestCase):

    def test_authentication_token(self):
        api = TeslaAPI()

        token = api.refresh_access_token(
            username=os.getenv('username', ''),
            password=os.getenv('password', '')
        )

        assert token

    def test_routes(self):
        api = TeslaAPI()
        api.refresh_access_token(
            username=os.getenv('username', ''),
            password=os.getenv('password', '')
        )

        r = api.vehicles()
        assert r.status_code == 200