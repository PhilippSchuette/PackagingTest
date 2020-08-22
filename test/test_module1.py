import module1 as mod1
import pytest
from hypothesis import given
from hypothesis.strategies import integers


def test_func2():
    result = mod1.func2()
    assert result[0] == 2 * result[1]
    assert result[0] == 4 * result[2]
    assert result[0] == 8 * result[3]


def test_add():
    assert mod1.add(1, 2) == 3
    assert mod1.add(0, 0) == 0


@given(integers())
def test_add2(x):
    assert mod1.add(x, 0) == x


@given(integers(), integers())
def test_add3(x, y):
    assert mod1.add(x, y) == mod1.add(y, x)


def test_subtract():
    assert mod1.subtract(1, 2) == -1
    assert mod1.subtract(0, 0) == 0


def test_multiply():
    assert mod1.multiply(1, 2) == 2
    assert mod1.multiply(0, 0) == 0


def test_divide():
    assert mod1.divide(1, 2) == 0.5
    assert mod1.divide(1, 1) == 1
    with pytest.raises(ZeroDivisionError):
        mod1.divide(3.1415, 0)
