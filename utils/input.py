from pydantic import BaseModel, model_validator
from enum import Enum

class Types_d(Enum):
    NUMBER = "number"
    STRING = "string"
    BOOL = "boolean"
    INTERGER = "integer"


class Input_prompt(BaseModel):
    prompt: str

    def print_data(self) -> None:
        print("========THE=PROMPT========")
        print(f"{self.prompt["prompt"]}")
        print("==========================")

    def get_prompt(self) -> str:
        return self.prompt


class Input_definition(BaseModel):
    name: str
    description: str
    parameters: dict[str, dict[str, str]]
    returns: dict[str, str]

    @model_validator(mode="after")
    def parse(self) -> 'Input_definition':
        if not self.name.startswith("fn_"):
            raise ValueError("The name should start with 'fn_'")
        self.verif_key_type()
        self.verif_type(tab_list = [
            Types_d.NUMBER.value,
            Types_d.STRING.value,
            Types_d.BOOL.value,
            Types_d.INTERGER.value,
        ])
        return self

    def verif_key_type(self) -> None:
        for k, v in self.parameters.items():
            for key in v.keys():
                if key != "type":
                    raise KeyError(f"In the definition {self.name} "
                                   " the key is not in the good format and should"
                                   " be 'type'")
        for key in self.returns.keys():
            if key != "type":
                raise KeyError(f"In the definition {self.name} "
                                " the key is not in the good format and should"
                                " be 'type'")

    def verif_type(self, tab_list: list[str]) -> None:
        for k, v in self.parameters.items():
            if v["type"] not in tab_list:
                raise ValueError("The type value is forbidden in the definition "
                                 f"{self.name}")

    def get_definitions_format_str(self) -> str:
        data = "{"
        data += (f"name : {self.name}, ")
        data += (f"description {self.description}, ")
        data += (f"parameters: {str(self.parameters)}, ")
        data += (f"returns : {str(self.returns)}, ")
        data += "}\n"
        return data

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_parameters(self) -> dict[str, dict[str, str]]:
        return self.parameters

    def get_returns(self) -> dict[str, str]:
        return self.returns