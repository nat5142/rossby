from .base import BaseSession


class LDJsonSession(BaseSession):
    header_accept = 'ld+json'

    def __init__(self):
        super(LDJsonSession, self).__init__()
