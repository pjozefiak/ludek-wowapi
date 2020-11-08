import requests


class Connect:
    def __init__(self, region, endpoint, token, namespace, locale, **fields):
        self.region = region
        self.endpoint = endpoint
        self.token = token
        self.fields = fields
        self.namespace = namespace
        self.locale = locale

    def get_data(self):
        url = 'https://{}.api.blizzard.com{}'.format(self.region, self.endpoint)
        payload = {
            'namespace': self.namespace,
            'access_token': self.token,
            'locale': self.locale
        }
        r = requests.get(url, headers=self.token, params={**payload, **self.fields})
        return r.json()
