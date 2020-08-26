# This is the second module in my PackingTest repository. Here we have test
# implementations according to the ground rules set out in the README.

import math

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

    emp1 = mod1.Employee(1234, "John", "Smith")
