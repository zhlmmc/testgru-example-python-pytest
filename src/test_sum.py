import pytest
from src.sum import custom_sum

def test_custom_sum_empty_list():
    assert custom_sum([]) == 0

def test_custom_sum_single_number():
    assert custom_sum([5]) == 5

def test_custom_sum_positive_numbers():
    assert custom_sum([1, 2, 3, 4, 5]) == 15

def test_custom_sum_negative_numbers():
    assert custom_sum([-1, -2, -3]) == -6

def test_custom_sum_mixed_numbers():
    assert custom_sum([-2, 0, 3, -1, 4]) == 4

def test_custom_sum_floating_point():
    assert custom_sum([1.5, 2.5, 3.5]) == 7.5

def test_custom_sum_large_numbers():
    assert custom_sum([10000000, 20000000, 30000000]) == 60000000

def test_custom_sum_invalid_input():
    with pytest.raises(TypeError):
        custom_sum("not a list")

def test_custom_sum_invalid_elements():
    with pytest.raises(TypeError):
        custom_sum([1, "2", 3])

def test_custom_sum_none_input():
    with pytest.raises(TypeError):
        custom_sum(None)
