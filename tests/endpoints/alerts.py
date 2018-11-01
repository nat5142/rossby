from models.rossby import Rossby
import unittest


class TestAlertsEndpoint(unittest.TestCase):

    def setUp(self):
        self.rossby = Rossby()

    def tearDown(self):
        pass

    def test_base_alerts(self):
        params = {}
        alerts = self.rossby.alerts.get(params=params)
        assert type(alerts) == dict

    def test_active_alerts(self):
        params = {}
        active_alerts = self.rossby.alerts.get_active(params=params)
        assert len(active_alerts.get('features') > 0)

    def test_alerts_by_id(self):
        params = {}
        alert_id = 'NWS-IDP-PROD-KEEPALIVE-17819'
        alert_by_id = self.rossby.alerts.get_by_id(id='NWS-IDP-PROD-KEEPALIVE-17819')
        assert alert_by_id.get('id') == "https://api.weather.gov/alerts/NWS-IDP-PROD-3196042-2810355"

    def test_alerts_tyes(self):
        alert_types = self.rossby.alerts.get_types()
        assert type(alert_types.get('event_types')) == list

    def test_active_alert_count(self):
        alert_count = self.rossby.alerts.get_count()
        expected_keys = ['total', 'land', 'marine', 'regions', 'areas', 'zones']
        for exp in expected_keys:
            assert exp in alert_count.keys()
