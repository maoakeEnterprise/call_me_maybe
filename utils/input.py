from pydantic import BaseModel, model_validator


class Input_prompt(BaseModel):
    prompt: dict[str, str]

    def print_data(self) -> None:
        print("========THE=PROMPT========")
        print(f"{self.prompt["prompt"]}")
        print("==========================")


class Input_definition:
    name: str
    description: str
    parameters: dict[str, str]
    returns: dict[str, str]

    @model_validator(mode="after")
    def parse(self) -> 'Input_definition':
        if self.name.startswith("fn_"):
            raise NameError("The name function should start with fn_")
        if self.name == "fn_add_numbers":
            self.valid_len(strict_len = 2)
            self.verif_third_layer(type_v = "number")
        elif self.name == "fn_greet":
            self.valid_len(strict_len = 1)
            self.verif_key_second_layer(key_l = ["name"])
            self.verif_third_layer(type_v = "string")
        elif self.name == "fn_reverse_string":
            self.valid_len(strict_len = 1)
            self.verif_third_layer(type_v = "string")
        elif self.name == "fn_get_square_root":
            self.valid_len(strict_len = 1)
            self.verif_third_layer(type_v = "number")
        elif self.name == "fn_substitute_string_with_regex":
            self.valid_len(strict_len = 3)
            self.verif_key_second_layer(key_l=["source_string",
                                               "regex",
                                               "replacement"])
            self.verif_third_layer(type_v = "string")
        return self

    def valid_len(self, strict_len: int) -> None:
        if len(self.parameters) != strict_len:
            raise ValueError("Not the good len in parameters"
                             f"for this function {self.name}")

    def verif_third_layer(self, type_v: str) -> None:
        key_verif = "type"
        for item in self.parameters:
            for key in item.keys():
                if key != key_verif:
                    raise KeyError("The key do not correspond on the "
                                   "third layout and should be "
                                   "'type' in the function"
                                   f"{self.name}")
        for item in self.parameters:
            if item["type"] != type_v:
                raise TypeError("The type do not correspon with the function "
                                f"{self.name} in the params and should be "
                                f"{type_v}")

    def verif_key_second_layer(self, key_l: list) -> None:
        for key in self.parameters.keys():
            if key not in key_l:
                raise KeyError("The key do not correspond")
            key_l.remove(key)

    def verif_type_return(self, type_v: str) -> None:
        for key in self.returns.keys():
            if key != "type":
                raise KeyError("The key do not correspond")
        if self.returns["type"] != type_v:
            raise ValueError("Wrong type")
