"""
Tests the add() function of the calculator.abs
"""
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
