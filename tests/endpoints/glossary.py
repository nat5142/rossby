from tests.base_test import BaseTestClass


class TestGlossaryEndpoint(BaseTestClass):

    def test_glossary_endpoint(self):
        params = {}
        test_against = self.plain_request('glossary', params=params)

        content = self.rossby.glossary.get()

        assert test_against == content.json()
