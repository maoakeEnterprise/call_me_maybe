from llm_sdk import Small_LLM_Model
from utils import Parsing, Translator
import json
import numpy as np


def main():
    try:
        print("Hello from call!")
        prompt_data = Parsing.valid_json("data/input/function_calling_tests.json")
        functions = Parsing.valid_json("data/input/functions_definition.json")
        data = Translator()
        data.fill_definitions_list(functions)
        data.fill_prompt_list(prompt_data)
        data.run_all(functions)
    except (FileNotFoundError, IsADirectoryError) as e:
        print("===========================")
        print(f"File not do not exist -> {e}")
        print("===========================")
    except json.decoder.JSONDecodeError as e:
        print("===========WRONG====FORMAT")
        print(f"Message Error : {e}")
        print("==========================")
    except ValueError as e:
        print("======VALUE=ERROR==========")
        print(f"Message error {e}")
        print("===========================")
    except KeyError as e:
        print("========KEY=ERROR==========")
        print(f"Message error: {e}")
        print("===========================")


if __name__ == "__main__":
    main()
