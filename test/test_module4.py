import numpy as np  # type: ignore
import pytest

import sub_module.module4 as mod4


def test_func1():
    assert mod4.func1() is None


def test_func2():
    assert mod4.func2() is None


def test_func3():
    assert mod4.func3() == mod4.__package__


# this test only asserts that all numba accelerated functions actually run:
def test_numba():
    x = np.arange(100).reshape(10, 10)
    y = np.arange(1e8)

    try:
        mod4.go_fast(x)
        mod4.go_slow(x)
        mod4.np_sum(y)
        mod4.sum_parallel(y)
        mod4.sum_parallel_fast(y)
    except Exception:
        pytest.fail("Numba accelerated functions did not work correctly")
