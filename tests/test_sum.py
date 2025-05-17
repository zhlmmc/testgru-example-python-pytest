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
    numbers = [-10, 5, -3, 8, -1]
    assert custom_sum(numbers) == -1

def test_custom_sum_with_float_numbers():
    numbers = [1.5, 2.7, -3.2, 4.1]
    assert custom_sum(numbers) == pytest.approx(5.1)

def test_custom_sum_with_large_numbers():
    numbers = [1000000000, 2000000000, 3000000000]
    assert custom_sum(numbers) == 6000000000

def test_custom_sum_with_invalid_type():
    numbers = [1, "2", 3]
    with pytest.raises(TypeError):
        custom_sum(numbers)

def test_custom_sum_with_none_input():
    with pytest.raises(TypeError):
        custom_sum(None)
