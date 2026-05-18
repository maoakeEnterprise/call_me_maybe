from utils.input import Input_prompt, Input_definition
from llm_sdk import Small_LLM_Model
import numpy as np
import copy


class Translator():
    def __init__(self) -> None:
        self.prompt_list: list[Input_prompt] = []
        self.data_list: list[Input_definition]  = []

    def fill_definitions_list(self, data: list) -> None:
        for object in data:
            self.data_list.append(
                Input_definition(**object)
            )

    def fill_prompt_list(self, data: list) -> None:
        for object in data:
            self.prompt_list.append(
                Input_prompt(**object)
            )

    def get_global_prompt(self, data_load: list, request) -> str:
        
        prompt = f"""[SYSTEM]
        You are a strict function calling assistant.
        Your ONLY task is to look at the [USER PROMPT], select "
        "the correct function from the [AUTHORIZED DATA SCHEMA], "
        "and return a valid JSON object.

        The output JSON must contain:
        1. The "name" of the function.
        2. The exact text from the user prompt under the key "prompt".
        3. The extracted arguments with their actual values under the"
        " key "parameters".

        Do NOT include any introduction, explanation, markdown formatting, or markdown code blocks (like ```json).
        Return ONLY the raw JSON object.

        Expected Output Format Example:
        {{
        "name": "function_name",
        "prompt": "{request}",
        "parameters": {{
            "param_name_1": value1,
            "param_name_2": value2
        }}
        }}

        [AUTHORIZED DATA SCHEMA]
        {data_load}

        [USER PROMPT]
        {request}

        [OUTPUT JSON]"""
        return prompt

    def check_ending(self, token: int, model: Small_LLM_Model, nb: int) -> None:
        string = model.decode([token])
        if ("}" in string):
            return (1)
        return (0)

    def run_all(self, data_load: list):
        llm = Small_LLM_Model()
        sentence = []
        for request in self.prompt_list:
            sentence.append(self.run_ai(data_load, request, llm))
        
    def run_ai(self, data_load: list, request: str, model: Small_LLM_Model) -> str:
        prompt = self.get_global_prompt(data_load, request)
        token_sensor = model.encode(prompt)
        token_list = token_sensor[0].tolist()
        logits = model.get_logits_from_input_ids(token_list)
        next_token_id = np.argmax(logits)
        sentence = []
        print(f"Prompt : {request}")
        i = 0
        while(1):
            token_list.append(next_token_id)
            sentence.append(next_token_id)
            logits = model.get_logits_from_input_ids(token_list)
            next_token_id = np.argmax(logits)
            next_words = model.decode(sentence)
            if self.check_ending(next_token_id, model, i) == 1:
                i += 1
            if i == 2:
                break
        sentence.append(next_token_id)
        next_words = model.decode(sentence)
        print(f"Sentence :")
        print(next_words)
        return next_words
