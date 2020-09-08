# This is a Cython extension module for the PackagingTest library. The
# conversion into *.c and subsequent compilation into a *.so extension for
# regular (C)Python is automated in setup.py.
# cython: language_level=3

# define C function with Python interface:
cpdef int cy_fib(int n):
    cdef int a, b, i, tmp
    a, b = 1, 1
    for i in range(n):
        tmp = a
        a += b
        b = tmp
    return a


# define a pure Python function without type declarations for speed comp:
def py_fib(n):
    a, b = 1, 1
    for i in range(n):
        tmp = a
        a += b
        b = tmp
    return a
