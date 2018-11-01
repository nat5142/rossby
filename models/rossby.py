import endpoints


class Rossby(object):
    base_url = 'https://api.weather.gov/'

    def __init__(self):
        self.stations = endpoints.Stations()
        self.alerts = endpoints.Alerts()
        self.glossary = endpoints.Glossary()

        self.connected = False
