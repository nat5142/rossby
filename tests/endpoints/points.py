from tests.base_test import BaseTestClass


class TestPointsEndpoint(BaseTestClass):

    def test_point(self):
        params = {}
        test_against = self.plain_request('points/{point}'.format(point='40.0,-73.0'), params=params)

        content = self.rossby.points.get_point(point='40.0,-73.0')

        self.assertDictEqual(test_against, content.json)

    def test_point_stations(self):
        params = {}
        test_against = self.plain_request('points/{point}/stations'.format(point='40.0,-73.0'), params=params)

        content = self.rossby.points.get_stations(point='40.0,-73.0')

        self.assertDictEqual(test_against, content.json)

    def test_point_forecast(self):
        params = {}
        test_against = self.plain_request('points/{point}/forecast'.format(point='40.0,-73.0'), params=params)

        content = self.rossby.points.forecast(point='40.0,-73.0')

        self.assertDictEqual(test_against, content.json)

    def test_point_hourly(self):
        params = {}
        test_against = self.plain_request('points/{point}/forecast/hourly'.format(point='40.0,-73.0'), params=params)

        content = self.rossby.points.hourly_forecast(point='40.0,-73.0')

        self.assertDictEqual(test_against, content.json)
