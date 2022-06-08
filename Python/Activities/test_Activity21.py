import pytest


# test to check sum
def test_sum():
    num1 = 25
    num2 = 30
    assert num1 + num2 == 55


# test to check difference
def test_subtraction():
    num1 = 100
    num2 = 75
    assert num1 - num2 == 25


# test to check multiplication
def test_multiplication():
    num1 = 12
    num2 = 5
    assert num1 * num2 == 60


# test to check division
def test_division():
    num1 = 80
    num2 = 10
    assert num1 / num2 == 8
