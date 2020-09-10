# This is a Cython extension module for the PackagingTest library. The
# conversion into *.c and subsequent compilation into a *.so extension for
# regular (C)Python is automated in setup.py.
# cython: language_level=3

# this works locally, but lets Travis build fail:
# from mystruct cimport spam


# include pure C functions from `hello.c` as an example for inclusion of
# external/custom C libraries:
cdef extern from "hello.h":
    int add(int x, int y)


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


cpdef void hello(int x, int y):
    result = add(x, y)
    print(result)


cdef public float cube(float x):
    return x * x * x


# finally, declare a C function public for use in any C libraries linked with
# .pyx Cython file:
cdef public void say_hi_from_cy():
    print(f"My favorit number is {42}")
