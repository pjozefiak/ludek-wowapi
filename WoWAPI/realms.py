from WoWAPI import connector


class Realms:
    def __init__(self, region, token, namespace, locale):
        self.region = region
        self.token = token
        self.namespace = namespace
        self.locale = locale

    def get_realms(self):
        return connector.Connect(self.region, '/data/wow/realm/index', self.token, self.namespace,
                                 self.locale).get_data()
