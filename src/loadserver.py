import json
import os


class LoadServer:
    def __init__(self):
        self.json = None
        dirname = os.path.dirname(os.path.abspath(__file__))
        self.PATH = os.path.join(dirname, 'server/', 'smtp_servers.json')
        self.service_names = []

    def load(self):
        with open(self.PATH, "r") as file:
            self.json = json.load(file)

    def parse_json(self):
        self.load()
        for service in self.json:
            self.service_names.append(service)
