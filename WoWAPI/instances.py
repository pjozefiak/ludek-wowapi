from WoWAPI import connector
# Static namespace


class Instances:
    def __init__(self, region, token, namespace, locale, expansion_id):
        self.region = region
        self.token = token
        self.namespace = namespace
        self.locale = locale
        self.expansion_id = expansion_id

    def get_instances(self):
        return connector.Connect(self.region, '/data/wow/journal-expansion/{}'.format(self.expansion_id), self.token,
                                 self.namespace, self.locale).get_data()
