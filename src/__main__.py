# from llm_sdk import Small_LLM_Model
from utils import Parsing, Translator
import json


def main():
    try:
        print("Hello from call!")
        data1 = Parsing.valid_json("data/input/function_calling_tests.json")
        data2 = Parsing.valid_json("data/input/functions_definition.json")
        poop = Translator()
        poop.fill_data_list(data2)
        poop.fill_prompt_list(data1)
        print("Hello")
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
