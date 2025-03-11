import pytest
from src.sort import bubble_sort

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_random_list():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_duplicate_elements():
    assert bubble_sort([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

def test_bubble_sort_mixed_numbers():
    assert bubble_sort([-2, 0, 3, -1, 2]) == [-2, -1, 0, 2, 3]

def test_bubble_sort_floating_point():
    assert bubble_sort([3.14, 1.41, 2.71, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_bubble_sort_strings():
    assert bubble_sort(['d', 'c', 'b', 'a']) == ['a', 'b', 'c', 'd']

def test_bubble_sort_large_list():
    input_list = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    assert bubble_sort(input_list) == expected

def test_bubble_sort_none_elements():
    with pytest.raises(TypeError):
        bubble_sort([1, None, 3])

def test_bubble_sort_mixed_types():
    with pytest.raises(TypeError):
        bubble_sort([1, "2", 3])

def test_bubble_sort_non_list():
    with pytest.raises(TypeError):
        bubble_sort("not a list")

def test_bubble_sort_nested_lists():
    with pytest.raises(TypeError):
        bubble_sort([1, [2, 3], 4])
