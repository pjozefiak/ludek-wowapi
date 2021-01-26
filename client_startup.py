from tools import config
from WoWAPI import token
from tools.dumpers import dump_realms, dump_connected_realms, dump_expansions, dump_instances, dump_encounters


settings = config.Config('data/config.ini').get_config()
token = token.Token(settings['client'], settings['secret'], settings['region']).get_token()
region = settings['region']
locale = settings['locale']
expansion = settings['current_expansion']
dynamic_namespace = 'dynamic-{}'.format(region)
static_namespace = 'static-{}'.format(region)
profile_namespace = 'profile-{}'.format(region)


def client_init():
    print('Dumping realms...')
    dump_realms.dump_realms(region, token, dynamic_namespace, locale)
    print('Dumping realms - completed')
    print('---')

    print('Dumping connected realms')
    dump_connected_realms.dump_connected_realms(region, token, dynamic_namespace, locale)
    print('Dumping connected realms - completed')
    print('---')

    print('Dumping expansions indexes')
    dump_expansions.dump_expansions(region, token, static_namespace, locale)
    print('Dumping expansion indexes - completed')
    print('---')

    print('Dumping instances')
    dump_instances.dump_instances(region, token, static_namespace, locale)
    print('Dumping instances - completed')
    print('---')

    print('Dumping encounters')
    dump_encounters.dump_encounters(region, token, static_namespace, locale)
    print('Dumping encounters - completed')
    print('---')


print('Ludek WoW-API Client - client startup script')
print('---')
print('This script will populate client with base data needed. Press 1 to start.')
option = input()

if option == str(1):
    client_init()
else:
    print('Buh-bye')
    exit()
