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

def test_custom_sum_large_numbers():
    assert custom_sum([1000000, 2000000, 3000000]) == 6000000

def test_custom_sum_decimal_numbers():
    assert custom_sum([1.5, 2.7, 3.2]) == 7.4

def test_custom_sum_zero():
    assert custom_sum([0, 0, 0]) == 0
