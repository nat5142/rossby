from tests.base_test import BaseTestClass


class TestThumbnailsEndpoint(BaseTestClass):

    def test_thumbnail_by_area_endpoint(self):
        params = {}
        test_against = self.plain_request('thumbnails/satellite/PA', params=params)

        if test_against.get('status') == 500:
            # TODO: Log/output 500 error
            pass
        else:
            content = self.rossby.thumbnails.get_by_area(area='PA')
            self.assertDictEqual(test_against, content.json)
