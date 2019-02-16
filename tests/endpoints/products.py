from tests.base_test import BaseTestClass
import random


class TestProductsEndpoint(BaseTestClass):

    def test_base_products_with_limit_endpoint(self):
        params = {'limit': 50}
        test_against = self.plain_request('products', params=params)

        content = self.rossby.products.get(limit=50)

        self.assertDictEqual(test_against, content.json)

    def test_products_locations_endpoint(self):
        params = {}
        test_against = self.plain_request('products/locations', params=params)

        content = self.rossby.products.locations()

        self.assertDictEqual(test_against, content.json)

    def test_product_types_endpoint(self):
        params = {}
        test_against = self.plain_request('products/types', params=params)

        content = self.rossby.products.types()

        self.assertDictEqual(test_against, content.json)

    def test_product_by_id_endpoint(self):
        params = {'limit': 10}
        all_products = self.plain_request('products', params=params)

        product_id = all_products.get('@graph')[0].get('id')

        test_against = self.plain_request(f'products/{product_id}', params={})

        content = self.rossby.products.by_id(product_id=product_id)

        self.assertDictEqual(test_against, content.json)

    def test_product_by_type_endpoint(self):
        params = {}
        test_against = self.plain_request('products/types/AFD', params=params)

        content = self.rossby.products.by_type(type_id='AFD')

        self.assertDictEqual(test_against, content.json)

    def test_product_type_locations_endpoint(self):
        params = {}
        test_against = self.plain_request('products/types/AFD/locations', params=params)

        content = self.rossby.products.type_locations(type_id='AFD')

        self.assertDictEqual(test_against, content.json)

    def test_product_location_types_endpoint(self):
        params = {}
        forecast_discussion_locations = self.plain_request('products/types/AFD/locations', params=params)

        location_id = random.sample(forecast_discussion_locations.get('locations').items(), 1)[0][0]

        test_against = self.plain_request(f'products/locations/{location_id}/types', params=params)

        content = self.rossby.products.location_types(location_id=location_id)

        self.assertDictEqual(test_against, content.json)

    def test_products_by_type_and_location_endpoint(self):
        params = {}
        type_id = 'AFD'
        forecast_discussion_locations = self.plain_request(f'products/types/{type_id}/locations', params=params)

        location_id = random.sample(forecast_discussion_locations.get('locations').items(), 1)[0][0]

        test_against = self.plain_request(f'products/types/{type_id}/locations/{location_id}', params=params)

        content = self.rossby.products.by_type_and_location(type_id=type_id, location_id=location_id)

        self.assertDictEqual(test_against, content.json)
