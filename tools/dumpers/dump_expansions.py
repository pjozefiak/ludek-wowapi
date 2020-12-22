from WoWAPI import expansions
import yaml


def dump_expansions(region, token, namespace, locale):
    expansions_data = expansions.Expansions(region, token, namespace, locale).get_expansions()

    expansions_dict = {
        'expansions': {}
    }

    for expansion in expansions_data['tiers']:
        expansions_dict['expansions'][expansion['id']] = expansion['name']

    with open('data/expansions.yaml', 'w', encoding="utf-8") as realm_file:
        yaml.dump(expansions_dict, realm_file, allow_unicode=True)

    print('Realms dumped')