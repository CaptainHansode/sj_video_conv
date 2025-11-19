#!/usr/bin/env python3
"""tool config
"""
import collections
import json
import os


class ToolConfig(object):
    r"""汎用のコンフィグクラス
    """
    def __init__(self, file_path="", file_name="config.json", default={}):
        file_path = file_path or os.environ.get("USERPROFILE")
        self.path = os.path.join(file_path, file_name)
        self.dec = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
        self.data = default
        self.load()
        self.init_data(default)

    def save(self):
        r"""save"""
        with open(self.path, 'w') as save_file:
            json.dump(self.data, fp=save_file, indent=4)

    def load(self):
        r"""load"""
        if os.path.exists(self.path) is False:
            self.create_config_file()
        with open(self.path, 'r') as load_file:
            json_dict = json.load(
                load_file, object_pairs_hook=collections.OrderedDict)
        self.data = json_dict

    def create_config_file(self):
        r"""create"""
        if os.path.exists(os.path.dirname(self.path)) is False:
            os.makedirs(os.path.dirname(self.path))
        with open(self.path, 'w') as save_file:
            json.dump(self.data, fp=save_file, indent=4)

    def clear(self):
        r"""clear"""
        self.data = {}
        self.save()

    def init_data(self, config_data):
        r"""keys init
        """
        for k in config_data.keys():
            val = self.data.get(k)
            if val is None:
                self.data[k] = config_data[k]
        return None
