# type: ignore
# This is the first module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.

# standard library modules first
import math
import os


def func1():
    """
    :type: None
    :rtype: str
    """
    print(__name__)
    return __name__


def func2():
    """
    :type: None
    :rtype: List[float]
    """
    return [math.pi, math.pi / 2, math.pi / 4, math.pi / 8]


def func3():
    """
    :type: None
    :rtype: int
    """
    print(os.path)
    return 0


def add(x, y):
    """
    Adds two floats.

    :type x: float
    :param x: first summand
    :type y: float
    :param y: second summand
    :rtype: float
    """
    return x + y


def subtract(x, y):
    """
    Subtracts two floats.

    :type x: float
    :param x: positive
    :type y: float
    :param y: negative
    :rtype: float
    """
    return x - y


def multiply(x, y):
    """
    Multiplies two floats.

    :type x: float
    :param x: first factor
    :type y: float
    :param y: second factor
    :rtype: float
    """
    return x * y


def divide(x, y):
    """
    Divides two floats where the second must be non-zero, otherwise a
    ZeroDivisionError is raise.

    :type x: float
    :param x: numerator
    :type y: float != 0
    :param y: denominator
    :rtype: float
    """
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError
