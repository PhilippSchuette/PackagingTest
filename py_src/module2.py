# This is the second module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.
import logging
import math
import sys

import module1 as mod1
import module3 as mod3
from sub_module import module4 as mod4


def func1():
    """
    :type: None
    :rtype: None
    """
    print(__name__)


def func2():
    """
    :type: None
    :rtype: str
    """
    return "This is a random return string"


def tail(s):
    """
    Takes an input string and returns its tail, i.e. everything except the
    first element.

    :type: str
    :rtype: str
    """
    if len(s) > 0:
        return s[1:]
    # if s == "hi":
    #     return "hello"
    else:
        return ""


if __name__ == "__main__":
    x, y = 1.0, 2.0
    print(mod1.add(x, y))

    mod3.foo()
    mod4.func1()

    print(math.sqrt(1.0))

    # we can directly access the logger defined in module1 and e.g. set the
    # logging level by reading command line input:
    if len(sys.argv) > 1:
        if sys.argv[1] in ["debug", "info", "warning", "error", "critical"]:
            mod1.logger.setLevel(
                getattr(logging, sys.argv[1].upper())
            )

    emp1 = mod1.Employee(1234, "John", "Smith")
