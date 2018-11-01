from .base import BaseEndpoint
from .extensions import Observations, Radar


class Stations(BaseEndpoint):

    def __init__(self):
        self.observations = Observations()
        super(Stations, self).__init__()
        pass

    def get_all(self):
        pass
