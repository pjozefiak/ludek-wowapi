from WoWAPI import connector
# Static namespace


class Encounters:
    def __init__(self, region, token, namespace, locale, instance_id):
        self.region = region
        self.token = token
        self.namespace = namespace
        self.locale = locale
        self.instance_id = instance_id

    def get_encounters(self):
        return connector.Connect(self.region, '/data/wow/journal-instance/{}'.format(self.instance_id), self.token,
                                 self.namespace, self.locale).get_data()
