import pytest
from src.sort import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_order():
    assert bubble_sort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_duplicate_elements():
    assert bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-3, -1, -4, -2, -5]) == [-5, -4, -3, -2, -1]

def test_bubble_sort_mixed_numbers():
    assert bubble_sort([-2, 0, 3, -1, 2]) == [-2, -1, 0, 2, 3]

def test_bubble_sort_float_numbers():
    assert bubble_sort([3.14, 1.41, 2.71, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_bubble_sort_large_list():
    input_list = list(range(1000, 0, -1))  # 1000 to 1
    expected = list(range(1, 1001))  # 1 to 1000
    assert bubble_sort(input_list) == expected

def test_bubble_sort_none_elements():
    with pytest.raises(TypeError):
        bubble_sort([1, None, 3])

def test_bubble_sort_mixed_types():
    with pytest.raises(TypeError):
        bubble_sort([1, "2", 3])

def test_bubble_sort_non_list_input():
    with pytest.raises(TypeError):
        bubble_sort("not a list")
