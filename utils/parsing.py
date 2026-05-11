import json

class Parsing():

    @staticmethod
    def valid_data(file: str) -> bool:

        valid_key = {
            "prompt"
        }

        with open(file, "r") as f:
            data = json.load(f)
            for item in data:
                for key in item.keys():
                    if (key not in valid_key):
                        return False
        return True
