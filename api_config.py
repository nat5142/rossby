from collections import namedtuple
from functools import partial


response_types = {
    'geo+json': 'application/geo+json',
    'ld+json': 'application/ld+json',
    'dwml': 'application/vnd.noaa.dwml+xml',
    'oxml': 'application/vnd.noaa.obs+xml',
    'capxml': 'application/cap+xml',
    'atom': 'application/atom+xml'
}

APIEndpoint = namedtuple('APIEndpoint', 'endpoint method paginated response')
DefaultAPIEndpoint = partial(APIEndpoint, paginated=False, response=['geo+json'])
GETEndpoint = partial(DefaultAPIEndpoint, method='get')
GETPaginatedEndpoint = partial(GETEndpoint, paginated=True)


api_endpoints = {
    'alerts': {
        'get_all': GETPaginatedEndpoint('alerts', response=['ld+json', 'atom']),
        'active': GETEndpoint('alerts/active', response=['ld+json', 'atom']),
        'by_id': GETEndpoint('alerts/{id}', response=['ld+json', 'capxml']),
        'types': GETEndpoint('alerts/types', response=['ld+json']),
        'active_count': GETEndpoint('alerts/active/count', response=['ld+json']),
        'active_by_zone': GETEndpoint('alerts/active/zone/{zone_id}', response=['ld+json', 'atom']),
        'active_by_area': GETEndpoint('alerts/active/area/{area}', response=['ld+json', 'atom']),
        'active_by_region': GETEndpoint('alerts/active/region/{region}', response=['ld+json', 'atom'])
    },
    'glossary': {
        'get': GETEndpoint('glossary/', response=['geo+json'])
    },
    'gridpoints': {
        'wfo_xy': GETEndpoint('gridpoints/{wfo}/{x},{y}', response=['geo+json', 'ld+json']),
        'wfo_forecast': GETEndpoint('gridpoints/{wfo}/{x},{y}/forecast', response=['geo+json', 'ld+json']),
        'wfo_hourly': GETEndpoint('gridpoints/{wfo}/{x},{y}/forecast/hourly', response=['geo+json', 'ld+json']),
        'wfo_stations': GETEndpoint('gridpoints/{wfo}/{x},{y}/stations', response=['geo+json', 'ld+json'])
    },
    'icons': {
        'all': GETEndpoint('icons'),
        'get_icon': GETEndpoint('icons/{set}/{time_of_day}/{first}/{second}')
    },
    'thumbnails': {
        'get_by_area': GETEndpoint('thumbnails/satellite/{area}')
    },
    'stations': {
        'get_all': GETEndpoint('stations', response=['geo+json', 'ld+json']),
        'by_id': GETEndpoint('stations/{station_id}', response=['geo+json', 'ld+json']),
        'observations': GETEndpoint('stations/{station_id}/observations', response=['geo+json', 'ld+json']),
        'latest_observation': GETEndpoint('stations/{station_id}/observations/latest', response=['geo+json', 'ld+json']),
        'observation_by_time': GETEndpoint('stations/{station_id}/observations/{time}', response=['geo+json', 'ld+json']),
        'radar': GETEndpoint('stations/radar', response=['geo+json', 'ld+json']),
        'radar_by_id': GETEndpoint('stations/radar/{station_id}', response=['geo+json', 'ld+json'])
    },
    'offices': {
        'by_id': GETEndpoint('offices/{office_id}', response=['ld+json']),
        'headline_by_id': GETEndpoint('offices/{office_id}/headlines/{headline_id}', response=['ld+json']),
        'headlines': GETEndpoint('offices/office_id}/headlines', response=['ld+json'])
    },
    'points': {
        'get_point': GETEndpoint('points/{point}', response=['geo+json', 'ld+json']),
        'get_stations': GETEndpoint('points/{point}/stations', response=['geo+json', 'ld+json']),
        'forecast': GETEndpoint('points/{point}/forecast', response=['geo+json', 'ld+json', 'dwml']),
        'hourly_forecast': GETEndpoint('points/{point}/forecast/hourly', response=['geo+json', 'ld+json']),
    },
    'products': {
        'get': GETEndpoint('products', response=['ld+json']),
        'locations': GETEndpoint('products/locations', response=['ld+json']),
        'types': GETEndpoint('products/types', response=['ld+json']),
        'by_id': GETEndpoint('products/{product_id}', response=['ld+json']),
        'by_type': GETEndpoint('products/types/{type_id}', response=['ld+json']),
        'type_locations': GETEndpoint('products/types/{type_id}/locations', response=['ld+json']),
        'location_types': GETEndpoint('products/locations/{location_id}/types', response=['ld+json']),
        'by_type_and_location': GETEndpoint('products/types/{type_id}/locations/{location_id}', response=['ld+json'])
    },
    'zones': {
        'get': GETEndpoint('zones'),
        'by_type': GETEndpoint('zones/{type}', response=['geo+json', 'ld+json']),
        'by_type_and_zoneId': GETEndpoint('zones/{type}/{zone_id}', response=['geo+json', 'ld+json']),
        'zone_type_forecast': GETEndpoint('zones/{type}/{zone_id}/forecast', response=['geo+json', 'ld+json']),
        'forecast_observations': GETEndpoint('zones/forecast/{zone_id}/observations', response=['geo+json', 'ld+json']),
        'station_forecasts': GETEndpoint('zones/forecast/{zone_id}/stations', response=['geo+json', 'ld+json'])
    }
}