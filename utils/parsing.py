import json
from pydantic import BaseModel


class Parsing():

    @staticmethod
    def valid_json(file: str) -> dict:
        with open(file, "r") as f:
            data = json.load(f)
        return data