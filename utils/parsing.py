import json


class Parsing():

    @staticmethod
    def valid_json(file: str) -> list:
        with open(file, "r") as f:
            data = json.load(f)
        return data
