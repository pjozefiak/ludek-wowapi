from WoWAPI import instances_encounters
import yaml


def dump_encounters():
    with open('../../data/instances.yaml', 'r', encoding="utf-8") as expansions_file:
        instances_list = yaml.load(expansions_file, Loader=yaml.FullLoader)

    encounters_dict = {
        'instances': {}
    }

    print(instances_list)
    for expansion in instances_list['instances']:
        print(expansion)
        for dungeon in instances_list['instances'][expansion]['dungeons']:
            print(dungeon)

dump_encounters()