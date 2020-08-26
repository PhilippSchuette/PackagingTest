# type: ignore
# This is the first module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.
#
# This module implements a commmand line parser that reads a logging level if
# this module is executed directly. If you need to set the logging level from a
# module calling this one, directly access the logger as `module1.logger`.

# standard library modules first
import argparse
import logging
import math
import os
import subprocess
import webbrowser

# create logging directory if none exists:
if not os.path.exists("./logs/"):
    os.mkdir("./logs/")

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

f_handler = logging.FileHandler("./logs/mod1.log")
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
f_handler.setFormatter(formatter)


def get_parser():
    """ Set logging level from command line. """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--loglv", help="set the log-level for the module, default is `INFO`",
        default="info"
    )
    return parser


logger.addHandler(f_handler)


class Employee:
    """ Test class with some type checked attributes and some logging. """

    def __init__(self, id, first, last):
        """
        :type id: int
        :param id: employee id
        :type first: str
        :param first: employee's first name
        :type last: str
        :param last: employee's last name
        :rtype: instance of the `Employee` class
        """
        self.id = id
        self.first = first
        self.last = last
        logger.info(f"create Employee {last}, {first} (id: {id})")
        logger.debug("here goes debug information")
        logger.warning("this is a warning log")
        logger.error("this is an error log")
        logger.critical("this is a critical log")


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


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    logger.setLevel(getattr(logging, args.loglv.upper()))

    if not os.path.exists("./docs/html/index.html"):
        subprocess.run(["make", "html"], stdout=subprocess.DEVNULL)
    webbrowser.open(r"./docs/html/index.html", new=1)
