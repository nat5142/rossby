from models import Rossby


def test_get_all_stations():
    ross = Rossby()
    resp = ross.stations.get_all()
    assert len(resp.json().get('features')) == 2478
