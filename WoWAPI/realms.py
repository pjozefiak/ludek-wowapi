from WoWAPI import connector


class Realms:
    def __init__(self, region, token):
        self.region = region
        self.token = token

    def get_realms(self):
        return connector.Connect(self.region, '/data/wow/realm/index?locale=en_GB', self.token).get_data()
