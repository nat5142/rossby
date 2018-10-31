from models import Rossby


def test_connect_to_api():
	ross = Rossby()
	assert ross.connected is True


def test_station_query():
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
	ross = Rossby()
	assert ross.stations.get('KUNV') == test_against


def test_latest_observation():
	"""Query the stations/{station_id}/observations/latest endpoint for KUNV"""
	test_against = ['@context', 'id', 'type', 'geometry', 'properties']
	ross = Rossby()
	assert ross.stations.get('KUNV').observations.latest.keys() == test_against
