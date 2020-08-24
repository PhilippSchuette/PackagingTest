# This is the fourth module in my PackingTest repository; it is contained in
# the submodule `submodule`. Here we have test implementations according to the
# ground rules set out in the README.

from module1 import add
import module2 as mod2


def func1() -> None:
    """ Function printing the module name `sub_module.module4`. """
    print(__name__)


def func2() -> None:
    """ Function printing the complete path to file `module4`. """
    print(__file__)


def func3() -> str:
    """ Function returning the submodule name `sub_module`. """
    return __package__


if __name__ == "__main__":
    x, y = 1.0, 2.0
    print(add(x, y))

    print(mod2.func2())

    func3()
