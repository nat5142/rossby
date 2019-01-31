import builtins
import itertools
from addict import Dict


def format_key(key):
    strip = key.strip('@')
    return '{}_'.format(strip) if strip in itertools.chain(dir(builtins)) else strip


class RossbyResponse(Dict):

    def __init__(self, *args, **kwargs):
        super(RossbyResponse, self).__init__(*args, **kwargs)
        self.response = kwargs.get('response', None)

        for arg in args:
            if not arg:
                continue
            elif isinstance(arg, dict):
                for key, val in arg.items():
                    object.__setattr__(self, format_key(key), self._hook(val))
            elif isinstance(arg, tuple) and (not isinstance(arg[0], tuple)):
                pass
            else:
                for key, val in iter(arg):
                    object.__setattr__(self, format_key(key), self._hook(val))

        for key, val in kwargs.items():
            object.__setattr__(self, key, val)

    @classmethod
    def _hook(cls, item):
        if isinstance(item, dict):
            return cls(item)
        elif isinstance(item, list):
            return type(item)(cls._hook(elem) for elem in item)

        return item

    @property
    def json(self):
        return self.response.json()

    @property
    def next_page(self):
        return self.response.json().get('pagination', {}).get('next', None)

    def paginate(self):
        responses = []
        while self.next_page:
            _page = self.api.request_response(self.next_page, self.endpoint)
            self.response = _page.response
            responses.append(_page)

        return responses



class DefaultResponse(object):

    def __init__(self, api, endpoint, response):
        self.api = api
        self.endpoint = endpoint
        self.response = response
        self.first_response = True

    def json(self):
        return self.response.json()

    def __iter__(self):
        return self

    def __next__(self):
        if self.first_response:
            self.first_response = False

        if self.next_page:
            self.response = self.api.request_response(self.next_page, self.endpoint)
        else:
            raise StopIteration

        return self.response

    @property
    def next_page(self):
        return self.response.json().get('pagination', {}).get('next', None)
