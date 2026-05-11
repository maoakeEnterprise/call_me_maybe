# from llm_sdk import Small_LLM_Model
from utils import Parsing


def main():
    print("Hello from call!")
    valid_key = {
        "prompt",
    }
    print(Parsing.valid_data("data/input/function_calling_tests.json", valid_key))


if __name__ == "__main__":
    main()
