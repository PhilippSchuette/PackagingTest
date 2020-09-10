# simple example how to share C functions between different .pyx files
# cython: language_level=3

from extension1 cimport cube

print(cube(3.1415))
