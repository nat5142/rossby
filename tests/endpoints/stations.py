from tests.base_test import BaseTestClass


class TestStationsEndpoint(BaseTestClass):

    def test_base_endpoint(self):
        """Test base /stations endpoint"""
        assert len(self.rossby.stations.get_all().features) == 2784

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

        station_by_id = self.rossby.stations.get_by_id('KUNV')

        assert station_by_id.geometry == test_against

    def test_get_station_observation(self):
        params = {}
        test_against = self.plain_request('stations/KUNV/observations/', params=params).get('features')[0]['id']

        content = self.rossby.stations.get_observations('KUNV').features[0]['id']

        assert content == test_against

    def test_get_latest_station_observation(self):
        params = {}
        test_against = self.plain_request('stations/KUNV/observations/latest', params=params).get('properties')['@id']

        content = self.rossby.stations.get_latest('KUNV').properties['id']

        assert content == test_against

    def test_station_id_observation(self):
        """Test the /stations/{station_id}/observations endpoint"""
        params = {}
        test_against = None

        assert self.rossby.get('stations/KUNV/observations', params=params) == test_against
        assert self.rossby.stations('KUNV').observations().get(params=params) == test_against

    def test_station_id_latest_observation(self):
        """Test the /stations/{station_id}/observations/latest endpoint"""
        params = {}
        test_against = None

        assert self.rossby.stations('KUNV').observations().latest().get(params=params) == test_against

    def test_query_latest_for_all_stations_in_pennsylvania(self):
        pa_stations = self.rossby.stations(id='PA')
        pass
