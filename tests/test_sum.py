from src.sum import custom_sum
import pytest

def test_custom_sum_with_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    assert custom_sum(numbers) == 15

def test_custom_sum_with_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    assert custom_sum(numbers) == -15

def test_custom_sum_with_empty_list():
    numbers = []
    assert custom_sum(numbers) == 0

def test_custom_sum_with_floating_point():
    numbers = [1.5, 2.5, 3.5]
    assert custom_sum(numbers) == 7.5

def test_custom_sum_with_single_element():
    numbers = [42]
    assert custom_sum(numbers) == 42

def test_custom_sum_with_mixed_numbers():
    numbers = [-10, 5, -3, 8, -1]
    assert custom_sum(numbers) == -1

def test_custom_sum_with_invalid_input():
    with pytest.raises(TypeError):
        custom_sum(['a', 'b', 'c'])

def test_custom_sum_with_none():
    with pytest.raises(TypeError):
        custom_sum(None)

def test_custom_sum_with_mixed_types():
    with pytest.raises(TypeError):
        custom_sum([1, 'two', 3.0])
