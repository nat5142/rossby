from tests.base_test import BaseTestClass


class TestStationsEndpoint(BaseTestClass):

    def test_base_endpoint(self):
        """Test base /stations endpoint"""
        assert len(self.rossby.stations.get_all().features) == 2478

    def test_get_station_by_id(self):
        test_against = {
            "type": "Point",
            "coordinates": [
                -77.840100000000007,
                40.853439999999999
            ]
        }

        station_by_id = self.rossby.stations.by_id(station_id='KUNV')

        assert station_by_id.geometry.coordinates == test_against.get('coordinates')

    def test_get_station_observations(self):
        params = {}
        test_against = self.plain_request('stations/KUNV/observations/', params=params).get('features')[0].get('id')

        content = self.rossby.stations.observations(station_id='KUNV').features[0].get('id')

        assert content == test_against

    def test_get_latest_station_observation(self):
        params = {}
        test_against = self.plain_request('stations/KUNV/observations/latest', params=params).get('properties').get('@id')

        content = self.rossby.stations.latest_observation(station_id='KUNV').properties.id_

        assert content == test_against

    def test_get_radar(self):
        # TODO: Check to see if this endpoint is active again. Then, add rossby.radar.by_id() test
        params = {}
        test_against = self.plain_request('stations/radar', params=params)

        if test_against.get('status', '') and test_against.get('status') == 500:
            print(f'500 error encountered in {self.__class__.__name__}')
        else:
            content = self.rossby.stations.radar()
            self.assertDictEqual(test_against, content.json)
