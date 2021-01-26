from WoWAPI import instances_encounters
import yaml


def dump_encounters(region, token, namespace, locale):

    with open('data/instances.yaml', 'r', encoding="utf-8") as expansions_file:
        instances_list = yaml.load(expansions_file, Loader=yaml.FullLoader)

    def instances_list_generator(instance_type):
        instances_list_generated = []
        for dungeon in instances_list['instances'][expansion][instance_type]:
            instance = instances_encounters.Encounters(region, token, namespace, locale, dungeon).get_encounters()
            instance_dict = {
                instance['id']: {
                  'name': instance['name'],
                  'encounters': {}
                }
            }
            for encounter in instance['encounters']:
                instance_dict[instance['id']]['encounters'].update({encounter['id']: encounter['name']})
            instances_list_generated.append(instance_dict)
        return instances_list_generated

    for expansion in instances_list['instances']:
        encounters_dict = {
            'dungeons': {},
            'raids': {}
        }
        for dungeon in instances_list_generator('dungeons'):
            encounters_dict['dungeons'].update(dungeon)
        for raid in instances_list_generator('raids'):
            encounters_dict['raids'].update(raid)
        with open('data/expansions/{}/encounters.yaml'.format(expansion), 'w', encoding='utf-8') as encounters_file:
            yaml.dump(encounters_dict, encounters_file, allow_unicode=True)