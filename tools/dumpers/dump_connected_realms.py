from WoWAPI import connected_realms
import yaml


def dump_connected_realms(region, token, namespace, locale):
    realms_data = connected_realms.ConnectedRealms(region, token, namespace, locale)
    realms_dict = {
        'connected_realms': {}
    }
    for connected_realm in realms_data.get_connected_realms_id():
        realms_list = []
        print('Preparing Connected Realm: {}'.format(realms_data.get_connected_realm(connected_realm)['id']))
        for single_realm in realms_data.get_connected_realm(connected_realm)['realms']:
            realms_list.append(single_realm['id'])
        realm_string = ','.join(map(str, realms_list))
        realms_dict['connected_realms'][realms_data.get_connected_realm(connected_realm)['id']] = realm_string

        with open('data/connected_realms.yaml', 'w', encoding="utf-8") as realm_file:
            yaml.dump(realms_dict, realm_file, allow_unicode=True)
