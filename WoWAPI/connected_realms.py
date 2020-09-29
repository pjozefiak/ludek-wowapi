from WoWAPI import connector


class ConnectedRealms:
    def __init__(self, region, token, namespace):
        self.region = region
        self.token = token
        self.namespace = namespace
        self.connected_realms = self.get_connected_realms()

    def get_connected_realms(self):
        return connector.Connect(self.region, '/data/wow/connected-realm/index?locale=en_GB', self.token, self.namespace).get_data()

    def get_connected_realms_id(self):
        data = self.connected_realms['connected_realms']
        connected_realms_ids = []
        for realm in data:
            url_split = realm['href'].split('/')
            id_split = url_split[-1].split('?')
            connected_realms_ids.append(id_split[0])
        return connected_realms_ids

    def get_connected_realm(self, realm_id):
        return connector.Connect(self.region, '/data/wow/connected-realm/{}?locale=en_GB'.format(realm_id),
                                 self.token, self.namespace).get_data()
