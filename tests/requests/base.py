import unittest
from models.rossby import Rossby


class TestRequestors(unittest.TestCase):

    def test_atom_accept_headers(self):
        rossby = Rossby('atom')
        assert rossby.session_cls.headers['Accept'] == 'application/atom+xml'

    def test_cap_accept_headers(self):
        rossby = Rossby('cap')
        assert rossby.session_cls.headers['Accept'] == 'application/cap+xml'

    def test_dwml_accept_headers(self):
        rossby = Rossby('dwml')
        assert rossby.session_cls.headers['Accept'] == 'application/vnd.noaa.dwml+xml'

    def test_geojson_accept_headers(self):
        rossby = Rossby('geojson')
        assert rossby.session_cls.headers['Accept'] == 'application/geo+json'

    def test_default_accept_headers(self):
        rossby = Rossby()
        assert rossby.session_cls.headers['Accept'] == 'application/geo+json'

    def test_ldjson_accept_headers(self):
        rossby = Rossby('ldjson')
        assert rossby.session_cls.headers['Accept'] == 'application/ld+json'

    def test_oxml_accept_headers(self):
        rossby = Rossby('oxml')
        assert rossby.session_cls.headers['Accept'] == 'application/vnd.noaa.obs+xml'
