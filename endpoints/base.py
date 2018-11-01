

class BaseEndpoint(object):

	def __init__(self):
		pass

	def get(self, url, params={}):
		if not url:
			# query the default endpoint (i.e. /stations)
			pass
		else:
			# append the passed-in url extension to the default endpoint, send request
			pass

		return


