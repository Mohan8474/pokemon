from configparser import ConfigParser


class Config:
    def __init__(self, app):
        self.config_parser = ConfigParser()
        self.config = {}
        self.read_config(app)
        self.init_app(app)

    def read_config(self, app):
        self.config_parser.optionxform = str.upper
        self.config_parser.read("base.cfg")
        self.config = dict(self.config_parser["FLASK"])

    def init_app(self, app):
        app.config.update(self.config)

    # def __str__(self):
    #     return str(self.config)
