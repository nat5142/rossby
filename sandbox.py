from models.rossby import Rossby
from models.request import AtomXmlRequestor, CapXmlRequestor, DWMLRequestor, GeoJsonRequestor, LDJsonRequestor, \
    OXmlRequestor
#########################################################################################
#
# Desired commands for Rossby project -- each to be used as its own unittest
#
#########################################################################################


# ------------------------------------------------------------------------------------- #
# ------------------------------- Object initialization ------------------------------- #
# Creating a default Rossby instance (should default to application/geo+json) header
rossby = Rossby()
print(rossby.response_cls)  # outputs <models.request.geojson.GeoJsonRequestor object at 0x10fa59cf8>

# Create a Rossby instance to receive content in application/ld+json
rossby = Rossby(response_type=LDJsonRequestor)

# Create a Rossby instance to receive content in application/vnd.noaa.dwml+xml
rossby = Rossby(response_type=DWMLRequestor)

# Create a Rossby instance to receive content in application/vnd.noaa.obs+xml
rossby = Rossby(response_type=OXmlRequestor)

# Create a Rossby instance to receive content in application/cap+xml
rossby = Rossby(response_type=CapXmlRequestor)

# Create a Rossby instance to receive content in application/ld+json
rossby = Rossby(response_type=AtomXmlRequestor)
# ------------------------------------------------------------------------------------- #

rossby = Rossby()
# GET methods should return a Response object!!!
# i.e. alerts = rossby.alerts.get(params={})
# alerts.context = <'context' portion of response JSON>
# alerts.features = <'features' portion of response JSON>

# ------------------------------------------------------------------------------------- #
# ------------------------------- Alerts Endpoint Query ------------------------------- #
# Querying default endpoint /alerts with NO query parameters
alerts = rossby.alerts.get(params={})

# Querying the /alerts/active endpoint with NO query parameters
active_alerts = rossby.alerts.get_active(params={})  # needs a default limit
alert_ids = active_alerts.ids

# Querying the /alerts/{id} endpoint
alerts_by_id = rossby.alerts.get_by_id(id='NWS-IDP-PROD-KEEPALIVE-17819')  # does not take query params

# Querying the /alerts/types endpoint
alert_types = rossby.alerts.get_types()  # does not take query params
# should be a response object!!

# Querying the /alerts/active/count endpoint
alert_count = rossby.alerts.get_active_count()  # does not take query params

# Querying the /alerts/active/zone/{zone_id} endpoint
active_alerts_by_zone = rossby.alerts.get_active_by_zone(zone_id='AKC050')  # does not take query params

# Querying the /alerts/active/area/{area} endpoint
active_alerts_by_state = rossby.alerts.get_active_by_state(abbr='PA')  # does not take query params

# Querying the /alerts/active/region/{region} endpoint
active_alerts_by_marine_region = rossby.alerts.get_active_by_marine(abbr='PI')  # does not take query params


# ------------------------------------------------------------------------------------- #
# ------------------------------------- Glossary -------------------------------------- #
# Querying the /glossary endpoint
glossary = rossby.glossary.get()


# ------------------------------------------------------------------------------------- #
# ------------------------------------ Gridpoints ------------------------------------- #


# ------------------------------------------------------------------------------------- #
# -------------------------------------- Icons ---------------------------------------- #
# Query the /icons endpoint
icons = rossby.icons.get()  # does not take query params


# ------------------------------------------------------------------------------------- #
# ----------------------------------- Thumbnails -------------------------------------- #
# Query the /thumbnails/satellite/{area} endpoint
thumbnail = rossby.thumbnails.get_satellite_by_area(area='???')  # does not take query params


# ------------------------------------------------------------------------------------- #
# ------------------------------------ Stations --------------------------------------- #
# Query the /stations endpoint with NO query parameters
stations = rossby.stations.get()
station_id_list = stations.ids

# Query the /stations/radar/{station_id} endpoint
stations_by_id = rossby.stations.get_by_id(station_id='KUNV')  # does not take query params

# Query the /stations/radar endpoint
radar_stations = rossby.stations.get_radar_stations()  # does not take query params
radar_ids = radar_stations.ids

# Query the /stations/radar/{station_id} endpoint
radar_stations_by_id = rossby.stations.get_radar_by_id(station_id='???')  # does not take query params


