from .base import BaseSession


class CapXmlSession(BaseSession):
    header_accept = 'cap+xml'

    def __init__(self):
        super(CapXmlSession, self).__init__()
