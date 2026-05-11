# from llm_sdk import Small_LLM_Model
from utils import Parsing


def main():
    try:
        print("Hello from call!")
        print(Parsing.valid_json("data/input/function_calling_tests.json"))
        print(Parsing.valid_json("data/input/functions_definition.json"))
        print("Hello")
    except (FileNotFoundError, IsADirectoryError) as e:
        print("===========================")
        print(f"File not do not exist -> {e}")
        print("===========================")


if __name__ == "__main__":
    main()
