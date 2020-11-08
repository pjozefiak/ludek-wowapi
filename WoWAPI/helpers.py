import yaml


def get_connected_by_slug(slug):
    with open('data/connected_realms.yaml', 'r', encoding="utf-8") as realm_file:
        connected_data = yaml.load(realm_file, Loader=yaml.FullLoader)
        for value in connected_data['connected_realms'].values():
            for realms in value.split(","):
                print(realms)


def parse_items(items):
    equipped_items = {}
    for item in items['equipped_items']:
        equipped_items[item['slot']['name'].replace(' ', '_')] = {}
        equipped_items[item['slot']['name'].replace(' ', '_')]['id'] = item['item']['id']
        equipped_items[item['slot']['name'].replace(' ', '_')]['name'] = item['name']
        equipped_items[item['slot']['name'].replace(' ', '_')]['ilvl'] = item['level']['value']
    return equipped_items
