from my_json import json_my
from my_pickle import pickle_my
from my_toml import toml_my
from my_yaml import yaml_my


class SerializerFactory:

    def __init__(self):
        self.serializatorList = {
            "json": json_my(),
            "pickle": pickle_my(),
            "toml": toml_my(),
            "yaml": yaml_my()
            }

    def add(self, format, value):
         self.serializatorList.setdefault(format, value)

    def create_serializer(self, format):
        serialiser = self.serializatorList.get(format)
        if  serialiser is None:
            raise ValueError()
        else:
            return serialiser