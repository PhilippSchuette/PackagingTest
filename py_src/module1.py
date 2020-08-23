# type: ignore
# This is the first module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.

# standard library modules first
import math
import os


def func1():
    print(__name__)
    return __name__


def func2():
    return [math.pi, math.pi / 2, math.pi / 4, math.pi / 8]


def func3():
    print(os.path)
    return 0


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError
