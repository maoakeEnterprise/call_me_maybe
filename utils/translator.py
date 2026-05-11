from utils.input import Input_prompt, Input_definition


class Translator():
    def __init__(self):
        self.prompt_list: list[Input_prompt] = []
        self.data_list: list[Input_definition]  = []

    def fill_data_list(self, data: list):
        for object in data:
            self.data_list.append(
                Input_definition(**object)
            )

    def fill_prompt_list(self, data: list):
        for object in data:
            self.prompt_list.append(
                Input_prompt(**object)
            )