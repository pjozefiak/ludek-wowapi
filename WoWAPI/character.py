from WoWAPI import connector
from WoWAPI import helpers


class Character:
    def __init__(self, region, token, namespace, locale, realm, name):
        self.region = region
        self.token = token
        self.namespace = namespace
        self.locale = locale
        self.realm = realm
        self.name = name
        self.connect = self.connect

    def connect(self, endpoint):
        return connector.Connect(self.region, endpoint, self.token, self.namespace, self.locale).get_data()

    def get_character_base(self):
        char_base = self.connect('/profile/wow/character/{}/{}'.format(self.realm, self.name))
        char_equipment = self.connect('/profile/wow/character/{}/{}/equipment'.format(self.realm, self.name))
        char_media = self.connect('/profile/wow/character/{}/{}/character-media'.format(self.realm, self.name))
        char_data = {
            'id': char_base['id'],
            'name': char_base['name'],
            'display_name': char_base['active_title']['display_string'].replace('{name}', char_base['name']),
            'race': char_base['race']['name'],
            'class': char_base['character_class']['name'],
            'spec': char_base['active_spec']['name'],
            'realm': char_base['realm']['name'],
            'guild': char_base['guild']['name'],
            'level': char_base['level'],
            'achievements_points': char_base['achievement_points'],
            'last_login': char_base['last_login_timestamp'],
            'item_level_average': char_base['average_item_level'],
            'item_level_equipped': char_base['equipped_item_level'],
            'avatar': char_media['assets'][0]['value'],
            'equipped_items': helpers.parse_items(char_equipment)
        }
        return char_data
