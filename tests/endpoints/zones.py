from tests.base_test import BaseTestClass


class TestZonesEndpoint(BaseTestClass):

    def test_base_zones_endpoint_no_params(self):
        # TODO: Add test with params
        params = {}
        test_against = self.plain_request('zones', params=params)

        content = self.rossby.zones.get()

        self.assertDictEqual(test_against, content.json)

    def test_zones_by_type_endpoint(self):
        # TODO: Add test with params
        params = {}
        test_against = self.plain_request('zones/marine', params=params)

        content = self.rossby.zones.by_type(type='marine')

        self.assertDictEqual(test_against, content.json)

    def test_zones_by_type_and_id_endpoint(self):
        params = {}
        marine_zone = self.plain_request('zones/marine', params=params)

        zone_id = marine_zone.get('features')[0].get('id').split('/')[-1]

        test_against = self.plain_request(f'zones/forecast/{zone_id}', params=params)

        content = self.rossby.zones.by_type_and_zone_id(type='forecast', zone_id=zone_id)

        self.assertDictEqual(test_against, content.json)

    def test_zones_type_forecast_endpoint(self):
        # TODO: figure out how this endpoint works
        pass

    def test_zone_forecast_observations_endpoint(self):
        # TODO: Test with time constraints
        params = {}
        test_against = self.plain_request('zones/forecast/PAZ071/observations', params=params)

        content = self.rossby.zones.forecast_observations(zone_id='PAZ071')

        self.assertDictEqual(test_against, content.json)

    def test_zone_forecast_observations_with_limit_endpoint(self):
        # TODO: Test with time constraints
        params = {'limit': 10}
        test_against = self.plain_request('zones/forecast/PAZ071/observations', params=params)

        content = self.rossby.zones.forecast_observations(zone_id='PAZ071', limit=10)

        self.assertDictEqual(test_against, content.json)

    def test_zone_station_forecasts_endpoint(self):
        params = {}
        test_against = self.plain_request('zones/forecast/PAZ071/stations', params=params)

        content = self.rossby.zones.station_forecasts(zone_id='PAZ071')

        self.assertDictEqual(test_against, content.json)
