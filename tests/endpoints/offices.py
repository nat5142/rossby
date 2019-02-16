from tests.base_test import BaseTestClass


class TestOfficesEndpoint(BaseTestClass):

    def test_office_by_id_endpoint(self):
        params = {}
        test_against = self.plain_request('offices/CTP', params=params)

        content = self.rossby.offices.by_id(office_id='CTP')

        self.assertDictEqual(test_against, content.json)

    def test_headlines_endpoint(self):
        params = {}
        test_against = self.plain_request('offices/CTP/headlines', params=params)

        content = self.rossby.offices.headlines(office_id='CTP')

        self.assertDictEqual(test_against, content.json)

    def test_headline_by_id_endpoint(self):
        params = {}
        latest_headline = self.plain_request('offices/CTP/headlines', params=params)

        headline_id = latest_headline.get('@graph')[0].get('@id').split('/')[-1]
        test_against = self.plain_request(f'offices/CTP/headlines/{headline_id}', params=params)

        content = self.rossby.offices.headline_by_id(office_id='CTP', headline_id=headline_id)

        self.assertDictEqual(test_against, content.json)
