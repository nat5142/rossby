import unittest
from models.rossby import Rossby


class TestStationsEndpoint(unittest.TestCase):

	def setUp(self):
		self.ross = Rossby()

	def tearDown(self):
		pass

	def test_base_endpoint(self):
		"""Test base /stations endpoint"""
		assert len(self.ross.stations.get_all()['features']) == 2784

	def test_station_id_extension(self):
		"""Query the /stations/{station_id} endpoint, test coordinates are accurate for KUNV

		:return: none
		"""
		test_against = {
			"geometry": {
				"type": "Point",
				"coordinates": [
					-77.840100000000007,
					40.853439999999999
				]
			}
		}

		assert self.ross.stations.get('KUNV') == test_against
