import endpoints
from config import SESSION_CLASS_DICT


class Rossby(object):
    base_url = 'https://api.weather.gov/'

    def __init__(self, session_cls='default'):
        self.stations = endpoints.Stations()
        self.alerts = endpoints.Alerts()
        self.glossary = endpoints.Glossary()
        self.session_cls = SESSION_CLASS_DICT[session_cls]()

