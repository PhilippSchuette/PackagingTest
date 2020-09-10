# For a description of C data and function sharing between .pyx files see
# `extension1.pxd`
# `from extension1 cimport cube` does not work at the moment (for some unknown
# reason)...
# cython: language_level=3

# from extension1 cimport cube

# this is how to gain access to the NumPy C API:
# cimport numpy

# these work fine locally, but let Travis build fail:
from mystruct cimport spam
# cimport extension1


def print_cube():
    tmp = 3.1415
    print(tmp)
