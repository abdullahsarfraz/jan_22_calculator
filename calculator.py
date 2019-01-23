"""
A calculator library
"""

#def add(value1=0, value2=0):
#    return value1 + value2


def add(*args):
    """
    add() returns the sum of n-parameters
    """
    answer = 0
    for value in args:
        answer += value
    return answer
