import task2
import pytest

@pytest.mark.parametrize("value,typ", [
    (task2.integer_example, int),
    (task2.float_example, float),
    (task2.string_example, str),
    (task2.boolean_example, bool),
])
def test_types(value, typ):
    assert isinstance(value, typ)