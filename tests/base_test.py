import unittest
from models.rossby import Rossby
import requests


class BaseTestClass(unittest.TestCase):
    rossby = Rossby()

    def plain_request(self, extension, params={}):
        session = requests.Session()
        resp = session.get(self.rossby.base_url + extension, params=params)

        return resp.json()
