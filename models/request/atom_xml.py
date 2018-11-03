from .base import BaseSession


class AtomXmlSession(BaseSession):
    header_accept = 'atom+xml'

    def __init__(self):
        super(AtomXmlSession, self).__init__()
