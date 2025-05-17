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

def test_custom_sum_with_mixed_numbers():
    numbers = [-1, 2, -3, 4, -5]
    assert custom_sum(numbers) == -3

def test_custom_sum_with_single_element():
    numbers = [42]
    assert custom_sum(numbers) == 42

def test_custom_sum_with_floating_points():
    numbers = [1.5, 2.5, 3.5]
    assert custom_sum(numbers) == 7.5

def test_custom_sum_with_invalid_input():
    numbers = [1, "2", 3]
    with pytest.raises(TypeError):
        custom_sum(numbers)

def test_custom_sum_with_large_numbers():
    numbers = [1000000, 2000000, 3000000]
    assert custom_sum(numbers) == 6000000

def test_custom_sum_with_zero():
    numbers = [0, 0, 0]
    assert custom_sum(numbers) == 0

def test_custom_sum_with_small_decimals():
    numbers = [0.1, 0.2, 0.3]
    assert abs(custom_sum(numbers) - 0.6) < 1e-10
