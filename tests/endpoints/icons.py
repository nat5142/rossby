from tests.base_test import BaseTestClass


class TestIconsEndpoint(BaseTestClass):

    def test_base_icons_endpoint(self):
        params = {}
        test_against = self.plain_request('icons', params=params)

        content = self.rossby.icons.all()

        self.assertDictEqual(test_against, content.json)

    def test_static_icon_endpoint(self):
        params = {'size': 'medium'}
        test_against = self.icon_request('icons/land/night/ovc', params=params)

        content = self.rossby.icons.static_icon(set='land', time='night', condition='ovc', size='medium')

        self.assertEqual(test_against.content, content.content)

    def test_transition_icon_endpoint(self):
        params = {'size': 'medium'}
        test_against = self.icon_request('icons/land/night/ovc/rain', params=params)

        content = self.rossby.icons.transition_icon(set='land', time='night', first_condition='ovc',
                                                    second_condition='rain', size='medium')

        self.assertEqual(test_against.content, content.content)
