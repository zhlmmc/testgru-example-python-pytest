from src.sum import custom_sum

def test_custom_sum_with_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    assert custom_sum(numbers) == 15

def test_custom_sum_with_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    assert custom_sum(numbers) == -15
