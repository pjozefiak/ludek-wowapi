from WoWAPI import instances_encounters
import yaml


def dump_encounters(region, token, namespace, locale):
    with open('data/instances.yaml', 'r', encoding="utf-8") as expansions_file:
        instances_list = yaml.load(expansions_file, Loader=yaml.FullLoader)

    encounters_dict = {
        'dungeons': {},
        'raids': {},
    }

    print(instances_list)
    for expansion in instances_list['instances']:
        for dungeon in instances_list['instances'][expansion]['dungeons']:
            instance = instances_encounters.Encounters(region, token, namespace, locale, dungeon).get_encounters()
            print(instance['name'])
    print(encounters_dict)