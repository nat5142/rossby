import unittest
from models.rossby import Rossby


class TestPointsEndpoint(unittest.TestCase):

	def setUp(self):
		self.rossby = Rossby()

	def tearDown(self):
		pass

	def test_point(self):
		test_against = 'https://api.weather.gov/points/40,-73'
		params = {}
		latitude = 40.0
		longitude = -73.0
		point = self.rossby.points(lat=latitude, lon=longitude).get(params=params)
		assert point.json().get('properties')['@id'] == test_against

	def test_point_stations(self):
		test_against = 'https://api.weather.gov/stations/KISP'
		params = {}
		point = self.rossby.points(lat=40.0, lon=-73.0).stations(params=params)
		assert point.json().get('features')['id'] == test_against
