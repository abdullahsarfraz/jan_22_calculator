"""
Tests the add() function of the calculator.abs
"""
import pytest

from calculator import add

def test_two_plus_two():
    """
    if given 2 and 2 as parmeters, 4 shoud be returned
    """
    assert add(2, 2) == 4

def test_three_and_three():
    """
    if given 3 and 3, 6 should be returned
    """
    assert add(3, 3) == 6

def test_no_parameters():

    assert add() == 0

def test_one_two_three():
    """
    Given the values 1, 2 and 3 as parameters, 6 should be returned
    """
    assert add(1,2,3) == 6

def negative():
    """
    Given the values 1, 2 and 3 as parameters, 6 should be returned
    """
    assert add(-1, -1, -1, -1, -1) == -5

def test_decimal_values():
    """
    Assert that 0.1, 0.1 and 0.1 equals 0.3
    """
    assert add(0.1, 0.1, 0.1) == pytest.approx(0.3)
