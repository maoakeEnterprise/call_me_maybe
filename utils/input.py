from pydantic import BaseModel, model_validator


class Input_prompt(BaseModel):
    prompt: dict[str, str]

    def print_data(self) -> None:
        print("========THE=PROMPT========")
        print(f"{self.prompt["prompt"]}")
        print("==========================")


class Input_definition:
    name: dict[str, str]
    description: dict[str, str]
    parameters: dict[str, dict[str, str]]
    returns: dict[str, dict[str, str]]

    @model_validator(mode="after")
    def parse(self):
        print("test")
        if self.name["name"] == "fn_add_numbers":
            print()