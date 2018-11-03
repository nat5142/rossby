from .base import BaseSession


class DWMLSession(BaseSession):
    header_accept = 'vnd.noaa.dwml+xml'

    def __init__(self):
        super(DWMLSession, self).__init__()
