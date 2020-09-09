# This is the fourth module in my PackingTest repository; it is contained in
# the submodule `submodule`. Here we have test implementations according to the
# ground rules set out in the README.

from timeit import timeit

import numpy as np  # type: ignore

from numba import jit, prange  # type: ignore

from module1 import add
import module2 as mod2


x = np.arange(100).reshape(10, 10)
y = np.arange(1e8)


# setting `parallel=True` here actually slows down execution; with
# `fastmath=True`, `prange` instead of `range` and a higher number of
# dimensions (say 1e8 instead of 100) `parallel=True` can gain a factor of 2
# in speed:
@jit(nopython=True)
def go_fast(a):
    """
    Numba accelerated function doing computations on the main diagonal of
    an input NumPy array.
    """
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


def go_slow(a):
    """
    The same as `go_fast` but without Numba acceleration, i.e. @jit decorator.
    """
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


def np_sum(A):
    "Sum of square roots of entries of a NumPy array using np.dot."
    return np.sum(np.sqrt(A))


@jit(nopython=True, parallel=True)
def sum_parallel(A):
    "The same as np_sum but Numba accelerated and in parallel."
    n = len(A)
    acc = 0.0
    for i in prange(n):
        acc += np.sqrt(A[i])
    return acc


@jit(nopython=True, parallel=True, fastmath=True)
def sum_parallel_fast(A):
    "The same as sum_parallel but with `fastmath=True` enabled."
    n = len(A)
    acc = 0.0
    for i in prange(n):
        acc += np.sqrt(A[i])
    return acc


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
    result1 = timeit("go_fast(x)", setup="from __main__ import x, go_fast")
    result2 = timeit("go_slow(x)", setup="from __main__ import x, go_slow")
    result3 = timeit("np_sum(y)", globals=globals(), number=100)
    result4 = timeit("sum_parallel(y)", globals=globals(), number=100)
    result5 = timeit("sum_parallel_fast(y)", globals=globals(), number=100)

    print("fast result: ", result1)
    print("slow result: ", result2)
    print("np sum result: ", result3)
    print("parallel sum result: ", result4)
    print("fast parallel sum result: ", result5)

    x, y = 1.0, 2.0
    print(add(x, y))

    print(mod2.func2())

    func3()
