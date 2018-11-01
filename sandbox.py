from models import Rossby
from models.response import JsonLDResponse, DWMLResponse, OXMLResponse, CAPXmlResponse, ATOMXmlResponse
#########################################################################################
#
# Desired commands for Rossby project -- each to be used as its own unittest
#
#########################################################################################


# ------------------------------------------------------------------------------------- #
# ------------------------------- Object initialization ------------------------------- #
# Creating a default Rossby instance (should default to application/geo+json) header
rossby = Rossby()

# Create a Rossby instance to receive content in application/ld+json
rossby = Rossby(response_type=JsonLDResponse)

# Create a Rossby instance to receive content in application/vnd.noaa.dwml+xml
rossby = Rossby(response_type=DWMLResponse)

# Create a Rossby instance to receive content in application/vnd.noaa.obs+xml
rossby = Rossby(response_type=OXMLResponse)

# Create a Rossby instance to receive content in application/cap+xml
rossby = Rossby(response_type=CAPXmlResponse)

# Create a Rossby instance to receive content in application/ld+json
rossby = Rossby(response_type=ATOMXmlResponse)


# ------------------------------------------------------------------------------------- #

rossby = Rossby()
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
# should be a list -- see responses/alerts_types.json "event_types"

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


