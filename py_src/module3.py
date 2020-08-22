# type: ignore
# This is the third module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.


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
    return __file__
