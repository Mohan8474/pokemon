from configparser import ConfigParser

class Config:
    def __init__(self, app):
        self.config_parser = ConfigParser()
        self.config = {}
        self.read_config(app)

    def read_config(self, app):
        self.config_parser.read('base.cfg')
        self.config = dict(self.config_parser['DEFAULT'])
