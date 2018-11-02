from ..base_test import BaseTestClass


class TestAlertsEndpoint(BaseTestClass):

    def test_base_alerts(self):
        params = {}
        alerts = self.rossby.alerts.get(params=params)
        assert type(alerts) == dict

    def test_active_alerts(self):
        params = {}
        active_alerts = self.rossby.alerts.get_active(params=params)
        assert len(active_alerts.get('features') > 0)

    def test_alerts_by_id(self):
        alert_id = 'NWS-IDP-PROD-KEEPALIVE-17819'
        alert_by_id = self.rossby.alerts.get_by_id(id=alert_id)
        assert alert_by_id.get('id') == "https://api.weather.gov/alerts/NWS-IDP-PROD-3196042-2810355"

    def test_alerts_tyes(self):
        alert_types = self.rossby.alerts.get_types()
        assert type(alert_types.get('event_types')) == list

    def test_active_alert_count(self):
        alert_count = self.rossby.alerts.get_count()
        expected_keys = ['total', 'land', 'marine', 'regions', 'areas', 'zones']
        for exp in expected_keys:
            assert exp in alert_count.keys()

    def test_active_alerts_by_zone(self):
        zone_id = 'PHZ123'
        test_against = 'Alenuihaha Channel; Maalaea Bay; Big Island Southeast Waters; ' \
                       'Pailolo Channel; Big Island Leeward Waters'
        active_alerts_by_zone = self.rossby.alerts.get_active_by_zone(id=zone_id)

        assert active_alerts_by_zone.get('features')[0]['properties']['areaDesc'] == test_against

    def test_active_alerts_by_area(self):
        area_id = 'PA'
        test_against = 'Current watches, warnings, and advisories for Pennsylvania'
        active_alerts_by_area = self.rossby.alerts.get_active_by_area(id=area_id)

        assert active_alerts_by_area.get('title') == test_against

    def test_active_alerts_by_region(self):
        area_id = 'PI'
        test_against = 'Current watches, warnings, and advisories for Pacific Islands marine zones'
        active_alerts_by_region = self.rossby.alerts.get_active_by_region(id=area_id)

        assert active_alerts_by_region.get('title') == test_against
