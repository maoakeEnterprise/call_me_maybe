import pytest
from utils import Parsing, Input_definition, Input_prompt, Translator
import json

class TestParsing:

    def test_load_error(self):
        with pytest.raises(IsADirectoryError):
            Parsing.valid_json("data/input/")
    
    def test_load_error_1(self):
        with pytest.raises(FileNotFoundError):
            Parsing.valid_json("data/input/test.json")

    def test_valid_json_returns_list(self):
        data = Parsing.valid_json("data/input/functions_definition.json")
        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["name"].startswith("fn_")

    def test_input_prompt_valid(self):
        prompt = Input_prompt(prompt="Hello world")
        assert prompt.prompt == "Hello world"

    def test_input_definition_valid(self):
        definition = Input_definition(
            name="fn_example",
            description="Example function",
            parameters={"x": {"type": "number"}},
            returns={"type": "number"},
        )
        assert definition.name == "fn_example"
        assert definition.parameters["x"]["type"] == "number"

    def test_input_definition_invalid_name(self):
        with pytest.raises(ValueError):
            Input_definition(
                name="example",
                description="Missing fn_ prefix",
                parameters={"x": {"type": "number"}},
                returns={"type": "number"},
            )

    def test_input_definition_invalid_parameter_key(self):
        with pytest.raises(KeyError):
            Input_definition(
                name="fn_invalid_key",
                description="Invalid parameter key",
                parameters={"x": {"type": "number", "foo": "bar"}},
                returns={"type": "number"},
            )

    def test_input_definition_invalid_type(self):
        with pytest.raises(ValueError):
            Input_definition(
                name="fn_invalid_type",
                description="Invalid type",
                parameters={"x": {"type": "not_a_type"}},
                returns={"type": "number"},
            )

    def test_translator_fill_data_list(self):
        data = [
            {
                "name": "fn_add",
                "description": "Add values",
                "parameters": {"a": {"type": "number"}},
                "returns": {"type": "number"},
            }
        ]
        translator = Translator()
        translator.fill_data_list(data)
        assert len(translator.data_list) == 1
        assert translator.data_list[0].name == "fn_add"

    def test_translator_fill_prompt_list(self):
        prompts = [{"prompt": "Say hello"}]
        translator = Translator()
        translator.fill_prompt_list(prompts)
        assert len(translator.prompt_list) == 1
        assert translator.prompt_list[0].prompt == "Say hello"

    def test_json_error(self):
        with pytest.raises(json.decoder.JSONDecodeError):
            Parsing.valid_json("json_error/error.json")
