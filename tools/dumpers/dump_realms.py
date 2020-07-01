from WoWAPI import realms
import yaml


def dump_realms(region, token):
    realms_data = realms.Realms(region, token).get_realms()

    realms_dict = {
        'realms': {}
    }

    for realm in realms_data['realms']:
        realms_dict['realms'][realm['slug']] = {
            'id': realm['id'],
            'name': realm['name']
        }

    with open('data/realms.yaml', 'w', encoding="utf-8") as realm_file:
        yaml.dump(realms_dict, realm_file, allow_unicode=True)

    print('Realms dumped')
