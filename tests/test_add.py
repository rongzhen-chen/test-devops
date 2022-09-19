import pytest
from add_test import add

@pytest.mark.parametrize("test_input1, test_input2, expected", [
    (1, 2, 3),
    (-1, 1, 0),
])
def test_add(test_input1, test_input2, expected):
    assert add(test_input1, test_input2) == expected

