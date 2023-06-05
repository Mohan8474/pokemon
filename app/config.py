import configparser
import json


class Config:
    def __init__(self, app):
        self.config_parser = configparser.RawConfigParser()
        self.config = {}
        self.read_config(app)
        self.init_app(app)

    def read_config(self, app):
        self.config_parser.optionxform = lambda option : option
        self.config_parser.read("base.cfg")
        self.config = dict(self.config_parser["FLASK"])

    def init_app(self, app):
        result = {}
        for key, value in self.config.items():
            try:
                result[key] = json.loads(value)
            except json.JSONDecodeError as e:
                raise Exception("JSONDecodeError occurred:", e)
        app.config.update(result)

    # def __str__(self):
    #     return str(self.config)

