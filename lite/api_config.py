from collections import namedtuple
from functools import partial


APIEndpoint = namedtuple('APIEndpoint', 'endpoint method paginated')
DefaultAPIEndpoint = partial(APIEndpoint, paginated=False)
GETEndpoint = partial(DefaultAPIEndpoint, method='get')
GETPaginatedEndpoint = partial(GETEndpoint, paginated=True)


api_endpoints = {
    'alerts': {
        'get_all': GETPaginatedEndpoint('alerts')
    },
    'stations': {
        'get_all': GETPaginatedEndpoint('stations'),
        'station': GETEndpoint('stations/{station_id}')
    }
}
