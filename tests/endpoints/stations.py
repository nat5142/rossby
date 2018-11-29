from tests.base_test import BaseTestClass
from requests.exceptions import HTTPError


class TestStationsEndpoint(BaseTestClass):

    def test_base_endpoint(self):
        """Test base /stations endpoint"""
        assert len(self.rossby.stations.get_all().features) == 2478

    def test_get_station_by_id(self):
        """Query the /stations/{station_id} endpoint, test coordinates are accurate for KUNV

        :return: none
        """
        test_against = {
            "type": "Point",
            "coordinates": [
                -77.840100000000007,
                40.853439999999999
            ]
        }

        station_by_id = self.rossby.stations.by_id(station_id='KUNV')

        assert station_by_id.geometry == test_against

    def test_get_station_observations(self):
        params = {}
        test_against = self.plain_request('stations/KUNV/observations/', params=params).get('features')[0]['id']

        content = self.rossby.stations.observations(station_id='KUNV').features[0]['id']

        assert content == test_against

    def test_get_latest_station_observation(self):
        params = {}
        test_against = self.plain_request('stations/KUNV/observations/latest', params=params).get('properties')['@id']

        content = self.rossby.stations.latest_observation(station_id='KUNV').properties['@id']

        assert content == test_against

    def test_get_radar(self):
        params = {}
        try:
            test_against = self.plain_request('stations/radar', params=params)
            content = self.rossby.stations.radar().json()
        except HTTPError as err:
            if err.response.status_code != '500':
                raise err

        assert content == test_against

