import json
import os
import sys

from appdirs import user_data_dir

data_path = user_data_dir("rd-usb", False)
os.makedirs(data_path, exist_ok=True)
config_file = f'{data_path}/config.json'

if getattr(sys, "frozen", False):
    static_path = f'{sys._MEIPASS}/static'
else:
    static_path = os.path.realpath(f'{os.path.dirname(__file__)}/../static')


class Config:
    data = {}

    def __init__(self):
        if os.path.exists(config_file):
            with open(config_file, "r") as file:
                try:
                    self.data = json.load(file)
                except ValueError:
                    pass

    def read(self, name, fallback=None):
        return self.data[name] if name in self.data else fallback

    def write(self, name, value, flush=True):
        self.data[name] = value
        if flush:
            self.flush()

    def flush(self):
        with open(config_file, "w") as file:
            json.dump(self.data, file, indent=True)
