import builtins
import itertools


def format_key(key):
    strip = key.strip('@')
    return '{}_'.format(strip) if strip in itertools.chain(dir(builtins)) else strip


class AttrDict(dict):

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @staticmethod
    def obj_from_nested_dict(data):
        if not isinstance(data, dict):
            return data
        else:
            return AttrDict({format_key(key): AttrDict.obj_from_nested_dict(data[key]) for key in data})


class DefaultResponse(object):

    def __init__(self, api, endpoint, response):
        self.__dict__ = AttrDict.obj_from_nested_dict(response.json())
        self.api = api
        self.endpoint = endpoint
        self.response = response

    def json(self):
        return self.response.json()
