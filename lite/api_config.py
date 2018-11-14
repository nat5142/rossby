from collections import namedtuple
from functools import partial


APIEndpoint = namedtuple('APIEndpoint', 'endpoint method paginated')
DefaultAPIEndpoint = partial(APIEndpoint, paginated=False)
GETEndpoint = partial(DefaultAPIEndpoint, method='get')
GETPaginatedEndpoint = partial(GETEndpoint, paginated=True)


api_endpoints = {
    'alerts': {
        'get_all': GETPaginatedEndpoint('alerts'),
        'active': GETEndpoint('alerts/active'),
        'by_id': GETEndpoint('alerts/{id}'),
        'types': GETEndpoint('alerts/types'),
        'active_count': GETEndpoint('alerts/active/count'),
        'active_by_zone': GETEndpoint('alerts/active/zone/{zone_id}'),
        'active_by_area': GETEndpoint('alerts/active/area/{area}'),
        'active_by_region': GETEndpoint('alerts/active/region/{region}')
    },
    'glossary': {
        'get': GETEndpoint('glossary/')
    },
    'gridpoints': {
        'wfo_xy': GETEndpoint('gridpoints/{wfo}/{x},{y}'),
        'wfo_forecast': GETEndpoint('gridpoints/{wfo}/{x},{y}/forecast'),
        'wfo_hourly': GETEndpoint('gridpoints/{wfo}/{x},{y}/forecast/hourly'),
        'wfo_stations': GETEndpoint('gridpoints/{wfo}/{x},{y}/stations')
    },
    'icons': {
        'get_icon': GETEndpoint('icons/{set}/{time_of_day}/{first}/{second}'),
        'all_icons': GETEndpoint('icons')
    },
    'thumbnails': {
        'get_by_area': GETEndpoint('thumbnails/satellite/{area}')
    },
    'stations': {
        'get_all': GETPaginatedEndpoint('stations'),
        'by_id': GETEndpoint('stations/{station_id}'),
        'observations': GETEndpoint('stations/{station_id}/observations'),
        'latest_observation': GETEndpoint('stations/{station_id}/observations/latest'),
        'observation_by_time': GETEndpoint('stations/{station_id}/observations/{time}'),
        'radar': GETEndpoint('stations/radar'),
        'radar_by_id': GETEndpoint('stations/radar/{station_id}')
    },
    'offices': {
        'by_id': GETEndpoint('offices/{office_id}'),
        'headline_by_id': GETEndpoint('offices/{office_id}/headlines/{headline_id}'),
        'headlines': GETEndpoint('offices/office_id}/headlines')
    },
    'points': {
        'get_point': GETEndpoint('points/{point}'),
        'get_stations': GETEndpoint('points/{point}/stations'),
        'forecast': GETEndpoint('points/{point}/forecast'),
        'hourly_forecast': GETEndpoint('points/{point}/forecast/hourly'),
    },
    'products': {
        'get': GETEndpoint('products'),
        'locations': GETEndpoint('products/locations'),
        'types': GETEndpoint('products/types'),
        'by_id': GETEndpoint('products/{product_id}'),
        'by_type': GETEndpoint('products/types/{type_id}'),
        'type_locations': GETEndpoint('products/types/{type_id}/locations'),
        'location_types': GETEndpoint('products/locations/{location_id}/types'),
        'by_type_and_location': GETEndpoint('products/types/{type_id}/locations/{location_id}')
    },
    'zones': {
        'get': GETEndpoint('zones'),
        'by_type': GETEndpoint('zones/{type}'),
        'by_type_and_zoneId': GETEndpoint('zones/{type}/{zone_id}'),
        'zone_type_forecast': GETEndpoint('zones/{type}/{zone_id}/forecast'),
        'forecast_observations': GETEndpoint('zones/forecast/{zone_id}/observations'),
        'station_forecasts': GETEndpoint('zones/forecast/{zone_id}/stations')
    }
}
