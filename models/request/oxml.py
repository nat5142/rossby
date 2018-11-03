from .base import BaseSession


class OXmlSession(BaseSession):
    header_accept = 'vnd.noaa.obs+xml'

    def __init__(self):
        super(OXmlSession, self).__init__()
