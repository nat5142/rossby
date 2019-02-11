from tests.base_test import BaseTestClass


class TestAlertsEndpoint(BaseTestClass):

    def test_base_alerts_endpoint(self):
        params = {'limit': 10}
        test_against = self.plain_request('alerts', params=params)

        content = self.rossby.alerts.get_all()

        # self.assertDictEqual(test_against, content.response.json())
        self.assertEqual(len(test_against.get('features')), len(content.features))

    def test_active_alerts(self):
        params = {}
        test_against = self.plain_request('alerts/active', params=params)

        content = self.rossby.alerts.active()

        self.assertEqual(test_against.keys(), content.response.json().keys())

    def test_get_alerts_active_count(self):
        params = {}
        test_against = self.plain_request('alerts/active/count', params=params)

        content = self.rossby.alerts.active_count()

        self.assertEqual(test_against.keys(), content.response.json().keys())

    def test_get_alerts_by_id(self):
        params = {}
        test_response = self.plain_request('alerts/active', params=params)
        test_id = test_response.get('features')[0].get('id').split('/')[-1]

        test_against = self.plain_request('alerts/{}'.format(test_id), params=params)

        content = self.rossby.alerts.by_id(id=test_id)

        self.assertEqual(test_against.keys(), content.response.json().keys())
