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

def test_custom_sum_with_single_element():
    numbers = [42]
    assert custom_sum(numbers) == 42

def test_custom_sum_with_mixed_numbers():
    numbers = [-10, 5, -3, 8, 0]
    assert custom_sum(numbers) == 0

def test_custom_sum_with_floating_point():
    numbers = [1.5, 2.7, -3.2, 0.5]
    assert abs(custom_sum(numbers) - 1.5) < 0.0001

def test_custom_sum_with_invalid_input():
    numbers = [1, 2, "3", 4, 5]
    with pytest.raises(TypeError):
        custom_sum(numbers)

def test_custom_sum_with_none_input():
    with pytest.raises(TypeError):
        custom_sum(None)
