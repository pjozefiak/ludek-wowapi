from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class Token:
    def __init__(self, client_id, client_secret, region):
        self.client_id = client_id
        self.client_secret = client_secret
        self.region = region

    def get_token(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = dict(oauth.fetch_token(token_url='https://{}.battle.net/oauth/token'.format(self.region),
                                       client_id=self.client_id, client_secret=self.client_secret))
        return {'Authorization': 'Bearer {}'.format(token['access_token'])}