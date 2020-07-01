from tools import config
from WoWAPI import token
from tools.dumpers import dump_realms, dump_connected_realms


settings = config.Config('data/config.ini').get_config()
token = token.Token(settings['client'], settings['secret'], settings['region']).get_token()


def client_init():
    print('Dumping realms...')
    dump_realms.dump_realms(settings['region'], token)
    print('Dumping realms - completed')
    print('---')
    print('Dumping connected realms')
    dump_connected_realms.dump_connected_realms(settings['region'], token)
    print('Dumping connected realms - completed')



print('Ludek WoW-API Client - client startup script')
print('---')
print('This script will populate client with base data needed. Press 1 to start.')
option = input()

if option == str(1):
    client_init()
else:
    print('Buh-bye')
    exit()