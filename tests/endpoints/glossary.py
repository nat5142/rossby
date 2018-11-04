import json
from tests.base_test import BaseTestClass


class TestGlossaryEndpoint(BaseTestClass):

    def test_glossary_endpoint(self):
        glossary = self.rossby.glossary()
        with open('./responses/glossary.json', 'r') as jfile:
            glossary_json = json.load(jfile)

        assert glossary == glossary_json
