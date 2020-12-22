from WoWAPI import connector
# Static namespace


class Expansions:
    def __init__(self, region, token, namespace, locale):
        self.region = region
        self.token = token
        self.namespace = namespace
        self.locale = locale

    def get_expansions(self):
        return connector.Connect(self.region, '/data/wow/journal-expansion/index', self.token, self.namespace,
                                 self.locale).get_data()
