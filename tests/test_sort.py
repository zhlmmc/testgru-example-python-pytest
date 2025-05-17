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

def test_bubble_sort_unsorted_list():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_with_duplicates():
    assert bubble_sort([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]

def test_bubble_sort_with_negative_numbers():
    assert bubble_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

def test_bubble_sort_mixed_numbers():
    assert bubble_sort([-2, 0, 3, -5, 7, 1]) == [-5, -2, 0, 1, 3, 7]

def test_bubble_sort_with_floats():
    assert bubble_sort([3.14, 2.71, 1.41, 1.73]) == [1.41, 1.73, 2.71, 3.14]

def test_bubble_sort_large_numbers():
    assert bubble_sort([1000000, 999999, 1000001]) == [999999, 1000000, 1000001]
