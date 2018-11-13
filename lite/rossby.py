import requests
from collections import namedtuple
from string import Formatter
from urllib.parse import urljoin
from .api_config import api_endpoints
from .resultset import ResultSet


class RossbyAPIMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'base_url' not in attrs:
            attrs['base_url'] = 'https://api.weather.gov/'

        attrs['__init__'] = RossbyAPIMeta.get_init_method()
        attrs['session'] = requests.session()
        attrs['formatter'] = Formatter()

        for attr, method in RossbyAPIMeta.get_request_methods():
            setattr(cls, attr, method)

        return super(RossbyAPIMeta, cls).__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        super(RossbyAPIMeta, self).__init__(name, bases, attrs)
        RossbyAPIMeta.generate_api_methods(self, attrs)

    @classmethod
    def get_init_method(cls):
        def __init__(self, response_type='application/geo+json'):
            self.session.headers['Accept'] = response_type

        return __init__

    @classmethod
    def get_request_methods(cls):
        def request(self, config, **kwargs):
            formatters = (formatter for _, formatter, _, _ in self.formatter.parse(config.endpoint) if formatter)
            url_params = {key: kwargs.pop(key) for key in formatters}
            url = urljoin(self.base_url, config.endpoint.format(**url_params))
            for key, value in kwargs.items():
                if type(value) in (list, tuple):
                    kwargs['key'] = ','.join(str(v) for v in value)
            params = {'params' if config.method == 'get' else 'data': kwargs}
            result = self.request_url(url, config, **params)
            return ResultSet(self, config, result) if config.paginated else result

        def request_url(self, url, config, **kwargs):
            response = self.session.request(config.method, url, **kwargs)
            response.raise_for_status()
            return response.json()

        yield 'request', request
        yield 'request_url', request_url

    @classmethod
    def generate_api_methods(cls, api, attrs):
        make_request = lambda config: lambda **kwargs: api.request(config, **kwargs)

        for obj_name, endpoints in api_endpoints.items():
            methods = {endpoint_name: make_request(config) for endpoint_name, config in endpoints.items()}
            APIMethod = namedtuple('APIMethod_{}'.format(obj_name), methods.keys())
            setattr(api, obj_name, APIMethod(**methods))


class Rossby(object, metaclass=RossbyAPIMeta):
    pass
