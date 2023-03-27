from src.pre_built.counter import count_ocurrences
import pytest
from unittest.mock import mock_open, patch


@pytest.fixture
def file():
    return """Jhuly, Jhuly, Samuel, Samuel"""


def test_counter(file):
    with patch("builtins.open", mock_open(read_data=file)):
        assert count_ocurrences("test", "jhuly") == 2
        assert count_ocurrences("test2", "samuel") == 2
