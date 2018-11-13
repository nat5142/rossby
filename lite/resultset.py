

class ResultSet(object):
    def __init__(self, api, config, result):
        self.api = api
        self.config = config
        self.result = result
        self.first_result = True

    def __iter__(self):
        return self

    def next(self):
        if self.first_result:
            self.first_result = False
        elif self.next_page:
            self.result = self.api.request_url(self.next_page, self.config)
        else:
            raise StopIteration
        return self.result

    @property
    def next_page(self):
        return self.result['response'].get('next_page')
