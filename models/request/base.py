from requests import Session


class BaseSession(Session):
    header_accept = 'geo+json'

    def __init__(self):
        super(BaseSession, self).__init__()
        self.headers.update({'Accept': f'application/{self.header_accept}'})
