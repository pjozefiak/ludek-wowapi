from WoWAPI import instances
import yaml


def dump_instances(region, token, namespace, locale):
    with open('data/expansions.yaml', 'r', encoding="utf-8") as expansions_file:
        expansions_list = yaml.load(expansions_file, Loader=yaml.FullLoader)

    instances_dict = {
        'instances': {}
    }

    for expansion in expansions_list['expansions']:
        print('Preparing Instances list for expansion: {}'.format(expansion))
        expac_instances = instances.Instances(region, token, namespace, locale, expansion).get_instances()
        expansion_dict = {
            'dungeons': {},
            'raids': {}
        }
        for dungeon in expac_instances['dungeons']:
            expansion_dict['dungeons'][dungeon['id']] = dungeon['name']

        for raid in expac_instances['raids']:
            expansion_dict['raids'][raid['id']] = raid['name']

        instances_dict['instances'][expansion] = expansion_dict

        with open('data/instances.yaml', 'w', encoding="utf-8") as instances_file:
            yaml.dump(instances_dict, instances_file, allow_unicode=True)
1