from src.sum import custom_sum
import pytest

def test_custom_sum_with_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    assert custom_sum(numbers) == 15

def test_custom_sum_with_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    assert custom_sum(numbers) == -15

def test_custom_sum_empty_list():
    numbers = []
    assert custom_sum(numbers) == 0

def test_custom_sum_single_element():
    numbers = [42]
    assert custom_sum(numbers) == 42

def test_custom_sum_floating_point():
    numbers = [1.5, 2.5, 3.5]
    assert custom_sum(numbers) == 7.5

def test_custom_sum_mixed_numbers():
    numbers = [-10, 5, -3, 8, -1]
    assert custom_sum(numbers) == -1

def test_custom_sum_large_numbers():
    numbers = [10**9, 10**9, 10**9]
    assert custom_sum(numbers) == 3 * 10**9

def test_custom_sum_invalid_input():
    numbers = [1, 2, "3", 4, 5]
    with pytest.raises(TypeError):
        custom_sum(numbers)

def test_custom_sum_none_input():
    with pytest.raises(TypeError):
        custom_sum(None)
