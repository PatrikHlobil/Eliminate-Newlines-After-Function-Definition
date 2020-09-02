from _pytest.config import directory_arg
import pytest
from pytest_check import check

from eliminate_newlines.core import (
    eliminate_newlines_after_function_definition_in_file,
    eliminate_newlines_after_function_definition_in_file_or_directory,
    eliminate_newlines_after_function_definition_in_string,
)

testcode0 = {
    "original": """
def foo(a):
    return a + 1

a=1+1
""",
    "formatted": """
def foo(a):
    return a + 1

a=1+1
""",
}

testcode1 = {
    "original": """
def foo(a):
        

    return a + 1

a=1+1
""",
    "formatted": """
def foo(a):
    return a + 1

a=1+1
""",
}


testcode2 = {
    "original": """
def test(a):
    
   return a + 1
   

class A:
    def test_this(a,
    b,
    c):
       

        return a + b + c
""",
    "formatted": """
def test(a):
   return a + 1
   

class A:
    def test_this(a,
    b,
    c):
        return a + b + c
""",
}


@pytest.mark.parametrize("code", [testcode1, testcode2])
def test_eliminate_newlines_after_function_definition_in_string(code):
    assert code["formatted"] == eliminate_newlines_after_function_definition_in_string(
        code=code["original"]
    )


class TestEliminateNewlinesAfterFunctionDefinitionInFile:
    @staticmethod
    @pytest.mark.parametrize(
        "code,expected_return_value", [[testcode0, 0], [testcode1, 1], [testcode2, 1]]
    )
    def test_eliminate_newlines_after_function_definition_in_file(
        code, expected_return_value, tmp_path
    ):

        filepath = tmp_path / "testfile.py"
        filepath.write_text(code["original"])

        return_value = eliminate_newlines_after_function_definition_in_file(
            path=filepath
        )

        with check:
            assert (
                filepath.read_text() == code["formatted"]
            ), "File not correctly formatted."
        with check:
            assert return_value == expected_return_value, "Return value is not correct"

    @staticmethod
    @pytest.mark.parametrize(
        "code,expected_return_value", [[testcode0, 0], [testcode1, 1], [testcode2, 1]]
    )
    def test_eliminate_newlines_after_function_definition_in_file__checkmode(
        code, expected_return_value, tmp_path
    ):

        filepath = tmp_path / "testfile.py"
        filepath.write_text(code["original"])

        return_value = eliminate_newlines_after_function_definition_in_file(
            path=filepath, check=True
        )

        with check:
            assert (
                filepath.read_text() == code["original"]
            ), "File should not be touched."
        with check:
            assert return_value == expected_return_value, "Return value is not correct"


class TestEliminateNewlinesAfterFunctionDefinitionInFileOrDirectory:
    @staticmethod
    @pytest.mark.parametrize(
        "code,expected_return_value", [[testcode0, 0], [testcode1, 1], [testcode2, 1]]
    )
    def test_eliminate_newlines_after_function_definition_in_file_or_directory__file(
        code,
        expected_return_value,
        tmp_path,
    ):
        filepath = tmp_path / "testfile.py"
        filepath.write_text(code["original"])

        return_value = (
            eliminate_newlines_after_function_definition_in_file_or_directory(
                path=filepath
            )
        )

        with check:
            assert (
                filepath.read_text() == code["formatted"]
            ), "File not correctly formatted."
        with check:
            assert return_value == expected_return_value, "Return value is not correct"

    @staticmethod
    def test_eliminate_newlines_after_function_definition_in_file_or_directory__directory(
        tmp_path,
    ):
        directory = tmp_path
        config = (
            [tmp_path / "testcode0.py", testcode0],
            [tmp_path / "testcode1.py", testcode1],
            [tmp_path / "testcode2.py", testcode2],
        )

        for filepath, content in config:
            filepath.write_text(content["original"])

        return_value = (
            eliminate_newlines_after_function_definition_in_file_or_directory(
                path=directory
            )
        )

        for filepath, content in config:
            with check:
                filepath.read_text() == content[
                    "formatted"
                ], "File not correctly formatted."
        with check:
            assert return_value == 1, "Return value is not correct"

    @staticmethod
    def test_eliminate_newlines_after_function_definition_in_file_or_directory__checkmode(
        tmp_path,
    ):
        directory = tmp_path
        config = (
            [tmp_path / "testcode0.py", testcode0],
            [tmp_path / "testcode1.py", testcode1],
            [tmp_path / "testcode2.py", testcode2],
        )

        for filepath, content in config:
            filepath.write_text(content["original"])

        return_value = (
            eliminate_newlines_after_function_definition_in_file_or_directory(
                path=directory
            )
        )

        for filepath, content in config:
            with check:
                filepath.read_text() == content[
                    "original"
                ], "File not correctly formatted."
        with check:
            assert return_value == 1, "Return value is not correct"
