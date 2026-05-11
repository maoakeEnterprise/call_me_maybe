# from llm_sdk import Small_LLM_Model
from utils import Parsing


def main():
    try:
        print("Hello from call!")
        valid_key = {
            "prompt",
        }
        print(Parsing.valid_data("data/input/", valid_key))
        print("Hello")
    except (FileNotFoundError, IsADirectoryError) as e:
        print("===========================")
        print(f"File not do not exist -> {e}")
        print("===========================")

if __name__ == "__main__":
    main()
