from WoWAPI import character, connected_realms, connector, helpers, realms, expansions, instances, \
    instances_encounters, token
from tools import config

settings = config.Config('../data/config.ini').get_config()
token = token.Token(settings['client'], settings['secret'], settings['region']).get_token()
region = settings['region']
locale = settings['locale']
expansion = settings['current_expansion']
dynamic_namespace = 'dynamic-{}'.format(region)
static_namespace = 'static-{}'.format(region)
profile_namespace = 'profile-{}'.format(region)
char_name = 'andeeria'
realm_name = 'argent-dawn'
instance_id = 1190

# Token Test
print('Testing token')
print('Token: {}\n'.format(token))

# Realm Test (dynamic)
print('Testing realms')
realms = realms.Realms(region, token, dynamic_namespace, locale).get_realms()
print('Realms: {}\n'.format(realms))

# Connected Realms Test (dynamic)
print('Testing connected realms')
con_realms = connected_realms.ConnectedRealms(region, token, dynamic_namespace, locale)
print('Get connected realms: {}'.format(con_realms.get_connected_realms()))
print('Get connected realms id: {}'.format(con_realms.get_connected_realms_id()))
print('Get connected realm (by id): {}\n'.format(con_realms.get_connected_realm('509')))

# Character Tests (profile)
print('Testing Character')
chara = character.Character(region, token, profile_namespace, locale, realm_name, char_name)
print('Get character base: {}\n'.format(chara.get_character_base()))

# Expansions Test (Index)
print('Testing Expansions Index')
expack = expansions.Expansions(region, token, static_namespace, locale)
print('Get expansions index: {}\n'.format(expack.get_expansions()))

# Instances Test (current expac)
print('Testing Current Expansions Instances')
instance = instances.Instances(region, token, static_namespace, locale, expansion)
print('Get current expansions instances: {}\n'.format(instance.get_instances()))

# Instances Encounter Test (Castle Nathria(
print('Testing Current Expansions Instances')
instance = instances_encounters.Encounters(region, token, static_namespace, locale, instance_id)
print('Get encounters for Castle Nathria: {}\n'.format(instance.get_encounters()))