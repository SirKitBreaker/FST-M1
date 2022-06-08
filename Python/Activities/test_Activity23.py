import pytest


# @pytest.fixture
# def input_value():
#     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     return numbers
#

def test_sum(input_value):
    sum = 0
    for num in input_value:
        sum = sum + num

    assert sum == 55
