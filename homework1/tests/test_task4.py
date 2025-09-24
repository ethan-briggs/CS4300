import pytest
from task4 import calculate_discount

@pytest.mark.parametrize("price,disc,expected", [
    (100, 10, 90.0),
    (200.0, 25, 150.0),
    (50, 0, 50.0),
])
def test_discount(price, disc, expected):
    assert calculate_discount(price, disc) == expected

def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

def test_non_numeric():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)