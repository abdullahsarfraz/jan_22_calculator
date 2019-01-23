"""
Tests the add() function of the calculator.abs
"""
from calculator import add

def test_two_plus_two():
    """
    if given 2 and 2 as parmeters, 4 shoud be returned
    """
    assert add(2, 2) == 4
