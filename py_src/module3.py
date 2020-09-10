# type: ignore
# This is the third module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.

import timeit

from extension1 import cy_fib, py_fib, hello


def foo():
    """
    This is a long docstring that actually doesn't convey any useful
    information.

    :type: None
    :rtype: None
    """
    print(__name__)


def bar():
    """
    Also a discription, this time with some basic **rst** syntax.
    """
    print(__package__)


def foo_bar():
    """
    :type: None
    :rtype: str
    """
    return __file__


if __name__ == "__main__":
    print(cy_fib(10))
    print(py_fib(10))
    hello(1, 2)

    res1 = timeit.timeit("cy_fib(10000)", number=10000, globals=globals())
    res2 = timeit.timeit("py_fib(10000)", number=10000, globals=globals())

    print(f"Cython version of Fibonacci sequence runs {res2 / res1}x faster")
