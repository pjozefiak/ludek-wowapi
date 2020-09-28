from WoWAPI import connector

class Character:
    def __init__(self, region, token, realm, name):
        self.region = region
        self.token = token,
        self.realm = realm,
        self.name = name

        def get_character_profile(self):
            return connector.Connect(self.region, '/profile/wow/character/{}/{}?locale=en_GB'.format(self.realm, self.name), self.token).get_data()