# this is a Cython `definition file`. Its purpose is similar to a .h header
# style for C programs; it is only needed when some .pyx `implementation file`
# or another .pxd file imports stuff from a second .pyx file (this second one
# needs the definition file). Such an import happens via the cimport keyword
# (often used with e.g. NumPy within .pyx implementation files).
# Implementations of C functions present in some .pxd file are automatically
# public for cimport; no need for `public` keyword (only need `public` for
# import into ordinary .c files!)


cdef float cube(float)
