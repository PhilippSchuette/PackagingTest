" Script illustrating how to use standardlib's tracemalloc to trace memory usage. "
import linecache
import sys
import tracemalloc

import numpy as np  # type: ignore


# define a very basic memory profiling decorator:
def mem_profiling(param=False):
    " Return a basic memory profiling decorator; does nothing if param=False. "
    def _profiling(func):
        def wrapped(*args, **kwargs):
            if param:
                tracemalloc.start()
                result = func(*args, **kwargs)
                current, peak = tracemalloc.get_traced_memory()
                print(f"Current in {func.__name__}: {current // 1024} kB")
                print(f"Peak in {func.__name__}: {peak // 1024} kB")
                tracemalloc.stop()
            else:
                result = func(*args, **kwargs)
            return result

        return wrapped

    return _profiling


def display_top(snapshot, key_type='lineno', limit=10) -> None:
    " Take memory snapshot, excluding 'frozen importlib._bootstrap', '<unknown>'. "
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


class SlottedClass:
    " Simple class with slots to demonstrate memory savings. "
    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a, b):
        " Initialize simple slotted class with parameters ``a, b``. "
        self.a = a
        self.b = b
        self.c = "hello"
        self.d = "world"


class NotSlottedClass:
    " Simple class without slots to compare to ``SlottedClass()``. "
    def __init__(self, a, b):
        " Initialize simple class without slots with parameters ``a, b``. "
        self.a = a
        self.b = b
        self.c = "hello"
        self.d = "world"


tracemalloc.start()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.append(10)
x.extend((10, 10, 10, 10, 10, 10, 10**200))
Y = 10**250
z = list(range(100000))

arr1 = np.array([x**2 for x in z])
arr2 = [x**2 for x in z]

obj1 = SlottedClass(arr1, arr1)
print(sys.getsizeof(obj1))
obj2 = NotSlottedClass(arr1, arr1)
print(sys.getsizeof(obj2))
obj2.c = 100
print(sys.getsizeof(obj2))

snap = tracemalloc.take_snapshot()
tracemalloc.stop()
display_top(snap)


@mem_profiling(True)
def square(arr):
    """
    Return a square version of the input array; input must support elementwise
    square. Contains creation and deletion of intermediate variables for testing
    purposes.
    """
    tmp = np.array(range(1000000))
    del tmp
    return arr ** 2


if __name__ == "__main__":
    in_arr = np.array(range(1000000))
    out_arr = square(in_arr)
