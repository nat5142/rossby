import unittest
from models.rossby import Rossby


class TestStationsEndpoint(unittest.TestCase):

	def setUp(self):
		self.ross = Rossby()

	def tearDown(self):
		pass

	def test_base_endpoint(self):
		"""Test base /stations endpoint"""
		assert len(self.ross.stations().get()['features']) == 2784

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

		assert self.ross.stations('KUNV') == test_against
		assert self.ross.stations.get('KUNV') == test_against

	def test_station_id_observation(self):
		"""Test the /stations/{station_id}/observations endpoint"""
		params = {}
		test_against = None

		assert self.ross.get('stations/KUNV/observations', params=params) == test_against
		assert self.ross.stations('KUNV').observations().get(params=params) == test_against

	def test_station_id_latest_observation(self):
		"""Test the /stations/{station_id}/observations/latest endpoint"""
		params = {}
		test_against = None

		assert self.ross.stations('KUNV').observations().latest().get(params=params) == test_against

	def test_query_latest_for_all_stations_in_pennsylvania(self):
		pa_stations = self.ross.stations(id='PA')
		pass
