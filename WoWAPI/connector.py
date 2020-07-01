import requests


class Connect:
    def __init__(self, region, endpoint, token, **fields):
        self.region = region
        self.endpoint = endpoint
        self.token = token
        self.fields = fields

    def get_data(self):
        url = 'https://{}.api.blizzard.com{}'.format(self.region, self.endpoint)
        payload = {
            'namespace': 'dynamic-{}'.format(self.region),
            'access_token': self.token
        }
        r = requests.get(url, headers=self.token, params={**payload, **self.fields})
        return r.json()