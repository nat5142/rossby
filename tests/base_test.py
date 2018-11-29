import unittest
from rossby import Rossby
import requests


class BaseTestClass(unittest.TestCase):
    rossby = Rossby()

    @staticmethod
    def plain_request(endpoint, params):
        session = requests.Session()
        resp = session.get(f"https://api.weather.gov/{endpoint}", params=params)

        return resp.json()
