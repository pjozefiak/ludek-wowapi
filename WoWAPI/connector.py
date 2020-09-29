import requests


class Connect:
    def __init__(self, region, endpoint, token, namespace, **fields):
        self.region = region
        self.endpoint = endpoint
        self.token = token
        self.fields = fields
        self.namespace = namespace

    def get_data(self):
        url = 'https://{}.api.blizzard.com{}'.format(self.region, self.endpoint)
        payload = {
            'namespace': self.namespace,
            'access_token': self.token
        }
        r = requests.get(url, headers=self.token, params={**payload, **self.fields})
        return r.json()