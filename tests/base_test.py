import unittest
from rossby import Rossby
import requests
import logging

logging.getLogger("urllib3").setLevel(logging.WARNING)


class BaseTestClass(unittest.TestCase):
    rossby = Rossby()

    @staticmethod
    def plain_request(endpoint, params):
        session = requests.Session()
        resp = session.get(f"https://api.weather.gov/{endpoint}", params=params)

        return resp.json()
