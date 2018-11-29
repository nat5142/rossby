from tests.base_test import BaseTestClass


class TestAlertsEndpoint(BaseTestClass):

    def test_base_alerts_endpoint(self):
        params = {}
        test_against = self.plain_request('alerts', params=params)

        content = self.rossby.alerts.get_all()

        assert test_against == content.json()
        assert test_against.get('features') == content.features
