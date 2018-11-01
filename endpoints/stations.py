from .base import BaseEndpoint
from .extensions import Observations, Radar


class Stations(BaseEndpoint):

    def __init__(self):
        self.observations = Observations()
        self.radar = Radar()
        super(Stations, self).__init__()

    def get_all(self):
        pass

