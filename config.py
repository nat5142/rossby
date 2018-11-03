from models.request import AtomXmlSession, CapXmlSession, DWMLSession, GeoJsonSession, LDJsonSession, \
    OXmlSession

SESSION_CLASS_DICT = {
    'atom': AtomXmlSession,
    'cap': CapXmlSession,
    'dwml': DWMLSession,
    'geojson': GeoJsonSession,
    'ldjson': LDJsonSession,
    'oxml': OXmlSession,

    'default': GeoJsonSession
}

