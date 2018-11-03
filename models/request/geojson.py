from .base import BaseSession


class GeoJsonSession(BaseSession):
    header_accept = 'geo+json'

    def __init__(self):
        super(GeoJsonSession, self).__init__()
