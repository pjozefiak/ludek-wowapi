import configparser


class Config:
    def __init__(self, config_file):
        self.config_file = config_file

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return {'client': config['Credentials']['API_CLIENT'], 'secret': config['Credentials']['API_SECRET'],
                'region': config['Settings']['BASE_REGION'], 'locale': config['Settings']['BASE_LOCALE'],
                'current_expansion': config['Settings']['CURRENT_EXPANSION']}
