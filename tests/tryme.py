from models import Rossby


def test_connect_to_api():
	ross = Rossby()
	assert ross.connected is True
