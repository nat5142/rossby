import endpoints


class Rossby(object):

    def __init__(self):
        self.stations = endpoints.Stations()
        self.alerts = endpoints.Alerts()
        self.glossary = endpoints.Glossary()

        self.connected = False
