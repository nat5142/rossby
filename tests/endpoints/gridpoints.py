from tests.base_test import BaseTestClass


class TestGridpointsEndpoint(BaseTestClass):

    def test_gridpoints_lat_lon_endpoint(self):
        params = {}
        office_id = 'PHI'
        lon = 40
        lat = 73
        test_against = self.plain_request(f'gridpoints/{office_id}/{lon},{lat}', params=params)

        content = self.rossby.gridpoints.point(office_id=office_id, lon=lon, lat=lat)

        self.assertDictEqual(test_against, content.json)

    def test_gridpoints_point_forecast_endpoint(self):
        params = {}
        office_id = 'PHI'
        lon = 40
        lat = 73
        test_against = self.plain_request(f'gridpoints/{office_id}/{lon},{lat}/forecast', params=params)

        content = self.rossby.gridpoints.forecast(office_id=office_id, lon=lon, lat=lat)

        self.assertDictEqual(test_against, content.json)

    def test_gridpoints_point_hourly_forecast_endpoint(self):
        params = {}
        office_id = 'PHI'
        lon = 40
        lat = 73
        test_against = self.plain_request(f'gridpoints/{office_id}/{lon},{lat}/forecast/hourly', params=params)

        content = self.rossby.gridpoints.hourly_forecast(office_id=office_id, lon=lon, lat=lat)

        self.assertDictEqual(test_against, content.json)

    def test_gridpoint_stations_endpoint(self):
        params = {}
        office_id = 'PHI'
        lon = 40
        lat = 73
        test_against = self.plain_request(f'gridpoints/{office_id}/{lon},{lat}/stations', params=params)

        content = self.rossby.gridpoints.stations(office_id=office_id, lon=lon, lat=lat)

        self.assertDictEqual(test_against, content.json)
