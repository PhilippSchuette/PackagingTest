================================
How to Package A Python3 Project
================================

.. image:: https://codecov.io/gh/PhilippSchuette/PackagingTest/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/PhilippSchuette/PackagingTest

.. image:: https://travis-ci.com/PhilippSchuette/PackagingTest.svg?branch=master
   :target: https://travis-ci.com/PhilippSchuette/PackagingTest

.. image:: https://img.shields.io/badge/Language-Python-blue.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/github/v/release/PhilippSchuette/PackagingTest
   :target: https://github.com/PhilippSchuette/PackagingTest

.. image:: https://img.shields.io/badge/docs-docstr--cov-success
   :target: https://pypi.org/project/docstr-coverage/

.. image:: https://img.shields.io/badge/mypy-checked-blue
   :target: https://mypy.readthedocs.io/en/stable/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

--------------------------------------------------------------------------------

.. contents:: Table of Contents
  :depth: 2

------------
Introduction
------------

**In an actual package documentation: Make rst highlighting syntax consistent!**

This package is a simple experiment involving the structural layout,
documentation, typing and testing facilities of an actual project like the
resonance related code in ``my_sage_repo``. All packages etc. should be installed
using *Pipenv* which ensures proper dependency management!

The GitHub respository was created and populated as follows:

  1. *$ git init*
  2. *$ git add --all*
  3. *$ git commit -m 'msg'*
  4. `Create repository on GitHub and copy <URL>`
  5. *$ git remote add origin <URL>*
  6. *$ git pull origin master --allow-unrelated-histories*
  7. *$ git push --set-upstream origin master*

--------------
Project Layout
--------------

The structure of the project is as follows:

    1. The *py_src/__init__.py* contains any code that should be executed whenever
       a module is imported and it is necessary for the build process
    2. *py_src/module1.py*, *py_src/module2.py*, *py_src/module3.py* are example modules
    3. *py_src/sub_module/module4.py* is an example for a submodule (every submodule
        directory must also contain an *__init__.py* script)

To update releases, first specify a git tag locally, then push it to remote and finally
use the GitHub UI to create a release from it (`recent release`, ...). For the first two
steps use

.. code:: bash

   $ git tag -a <vX.Y.Z> -m "tag msg"
   $ git push --follow-tags

Finally, you have to update the release version in `py_src/__init__.py`. This will automatically
update the version number in the documentation (`docs/conf.py`) as well as the `setup.py`. You
can embedded badges indicating the recent version as seen above.

**PyPI Version Badge:** use `https://img.shields.io/pypi/v/<package_name>`

**If you want to add modules or submodules:** Update *py_modules* in `setup.py` (and
maybe *requirements.txt* and even *install_requires*?).

---------------------
Handling Requirements
---------------------

Your install requirements should be specified in the `setup.py` (without version pinning).
To do so, make a clean virtual environment using *pipenv* and use the specifications from
the `Pipfile`. You should also specify *extra_requires*; these can e.g. be used to install
dev-requirements via

.. code:: bash

  $ python3 -m pip install -e .[dev]

-------------
Documentation
-------------

The documentation for the project is build with the
`Sphinx <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
*autodoc* utility. First, the general documentation structure was generated using

.. code:: bash

  $ sphinx-quickstart

You can generate documentation by simply typing

.. code:: bash

  $ make <builder>

where the two most commonly used builders are *html* and *latexpdf*. Omitting the
builder provides a list of available options (You can delete the Windows specific
make.bat file that is also automatically generated). You could also run something
like

.. code:: bash

  $ sphinx-build -b <builder> ./docs/ ./docs/

allowing you to specify the source and build directories manually (they are hard
coded in the Makefile). For some reason, latexpdf only works with the -M flag but
not with -b.

Now add **"sphinx.ext.autodoc"** to the extensions in your *conf.py* file. With the
directory structure as present in this project, you need to add the path to the
python modules relative to the conf.py file (i.e. ../py_src) to the path in your conf.py
as the autodoc directives won't work otherwise. You also have to include any
subdirectory of py_src separately.

The general logic goes as follows: For any Python module in py_src, add an associated
.rst file in docs containing at least a heading and an autodoc directive referencing
the module. The position of the .rst file in the toctree of index.rst determines the
position on the resulting documentation.

.. hint::
  index.rst contains examples on how to include LaTeX using the raw directive!

With *Makefile* the workflow is very simple: Type **make <builder>** and then **make clean**
to obtain complete documentation as *main.pdf* in *./docs*. For *<builder> = latexpdf* run
make twice to fix table of contents.

If you have cloned the repository and installed it locally, you can now use

.. code:: bash

   $ python3 -m module1

to directly open the html documentation in your default browser (**TODO:** fix the automatic
call to the documentation build process and the calling of the *index.html* to make this
functionality available for an installed project where the paths might be different from the
git repo layout)

----------
MyPy Stubs
----------

The stubs used for `MyPy <https://mypy.readthedocs.io/en/stable/>`_ static type
checking are contained within the subdirectory *stubs/*. You have to add this
directory to your ``MYPYPATH`` for type checking to work (or enable the correct
setting in an editor like atom).

*Commandline* type checking works with the following workflow from within the *py_src*
directory:

.. code:: bash

  $ export MYPYPATH='./stubs:$PROJECT_PATH/stubs:$PROJECT_NAME/stubs'
  $ mypy --config-file ../setup.cfg <module_name>

Here *<module_name>* could be either e.g. *module1.py* or *sub_module/module4.py*. At
the moment, the Atom MyPy plugin cannot resolve type annotations in *sub_module.module4*,
but this is suppressed with **ignore_missing_imports = True** in setup.cfg.

-------
Testing
-------

We will probably want to use `PyTest <https://docs.pytest.org/en/stable/contents.html>`_
together with `Hypothesis <https://hypothesis.readthedocs.io/en/latest/quickstart.html>`_
to implement so-called *property testing*.

With *Makefile* the workflow is easy: Type **make test** to run all tests and **make lint**
to run *MyPy* and *flake8*.

We have also implemented code coverage reports using pytest-cov; when running Travis
these reports are automatically uploaed to
`Codecov <https://docs.codecov.io/docs/quick-start>`_, where a visual inspection of
coverage is possible and a coverage badge for GitHub is created.

Finally, docstring coverage is automatically checked on every push to GitHub using
`docstr-coverage`. Any percentage `< 80%` (customizable) will fail the build process!

---------------
Logging Example
---------------

This repo also contains examples on how to implement some basic logging capabilities.
At the moment, logging is done in `module1.py` only. An example on how to manipulate
the logger of an imported package is contained in `module2.py`: Here we can set the
logger level of stuff imported from `module1.py` by giving a level on the command line.

Additionally, we present an example for CPU performance profiling in `sub_module.module4`.
At the moment, there is no working example for Memory profiling; `trace_mem.py` contains
first experiments in this direction using the standard library module `tracemalloc`. Once
running smoothly, this code should be integrated in e.g. `sub_module.module5.py`.

A (on first glance at least) very useful third-party tool for memory profiling is `Pympler`;
it provides facilities to get object sizes recursively and track either particular instances
or even whole classes by taking *snapshots*; this might be particularly useful in
combination with Jupyter Notebooks, as its API provides facilities for HTML formatted
statistics.

------------------------
Cython Extension Modules
------------------------

**Cython** extension modules provide a convenient way to combine the speed of **C** or
**C++** code with the advantages of pure (C)Python. There are several ways of using
**Cython**, but in this project you can simply type

.. code:: bash

  $ python3 setup.py build_ext --inplace

The current **Travis** build process generates the *.so* from scratch (i.e. from *.pyx*)
and the GitHub repo does not distribute the *.so* files. **Cython** is therefore a hard
dependency for the project and any potential user needs to have a C/C++ compiler installed
on their system.

**Note** that you can also include **Cython** type annotations via the ordinary Python
type annotation syntax:

.. code:: Python

  import cython
  ...
  def add(x: cython.int) -> cython.int:
        return x + 1

This syntax can also be mixed with ordinary (C)Python types e.g. dict, tuple, ...

We also have an example on how to use **Numba** decorators to speed up and parallelize
computations; these examples can be found in ``sub_module.module4``. For an actual
performance-critical project one could think about using a combination of **Cython**
and **Numba**, where the latter is more easily integrated in ordinary *CPython* code
that uses loops and *NumPy*.

We now have an example on how to call C libraries into a **Cython** .pyx file and, conversely,
how to call ``cdef public`` functions declared and defined in a .pyx file into a custom
C library (c.f. `extension1.pyx`, `hello.c`, `hello.h`, `module3.py`).

**Cython is now a hard dependency; any user has to have Cython installed on their system**

----------------
GPU Acceleration
----------------

A next step would be to add further parallel programming support (e.g. C/C++ extension
modules, Python Dask, multiprocessing, multithreading, async) or switch to GPU powered
computations (at least for performance critical sections?!). For GPU compatible drop-in
replacements with (almost) the NumPy API one could use **CuPy** (works on Nvidia's Cuda
architecture). Further research (mostly identifying critical sections and taking performance
measurements with simple drop-in replacements) is warranted here!

-------------
PyPI Workflow
-------------

The central tool for distributing packages on PyPI (*PYthon Package Index*) is twine:

.. code:: bash

  $ python3 -m pip install twine

The workflow is straight forward: Use

.. code:: bash

  $ python3 setup.py sdist bdist_wheel

to create a *dist/* directory with a source *tar*-archive and a source *wheel*. You should
check the contents of the source archives, e.g. with `tar tzf <...>.tar.gz`. You can check
if your package description renders properly with

.. code:: bash

  $ twine check dist/*

Finally, the actual upload happens with

.. code:: bash

  $ twine upload dist/*

This test package should actually not be upload to **PyPI** but to **TestPyPI** instead.
To do just this, add the `--repository testpypi` flag to the twine upload command. Now
test **pip** installations can be issued by adding the
`--index-url https://test.pypi.org/simple/` flag to the usual `pip3 install` command.
Giving the `--extra-index-url https://pypi.org/simple` allows pip to install dependencies
from the actual package index.

----------
Code Style
----------

To achieve a unified code style across all modules and submodules, you can use a tool called
**black** (``pip3 install black``). It is possible to either lint with black upon every push
or pull-request or to use a black plugin which lints on save. To achieve consistency you then
need to make sure that any core developer uses black and that any pull-request is edited by
a core developer before committing. The former way should therefore be preferred for a larger
project with many external contributors.

**Note** that compatibility between flake8 and black requires additional options, see *setup.cfg*.

==============================================
Summary -- What to copy into your next Project
==============================================

First, contemplate a directory structure based on the project layout and requirements; then,
make a `src` (or `py_src`, ...) folder and your structure inside it. Note, that you need an
``__init__.py``, maybe a ``__main__.py`` and your ``*.pyi`` stub files!

Next, the following option and setup files are necessary to achieve the functionality presented
in this repository:

  1. **setup.py** and **setup.cfg**
  2. **README.rst**, **LICENSE**, **MANIFEST.in** (, **CODE_OF_CONDUCT.rst**, **CONTRIBUTING.rst**)
  3. **.codecov.yml**, **.travis.yml**, **.coverage**
  4. **Makefile**
  5. **docs** folder and working *Sphinx* setup (just copy and adapt the stuff in this chapter!)
  6. a **test** folder with your unit tests (don't forget the ``__init__.py``)
  7. optionally a **utils** folder with binaries executables, etc.
  8. optionally a **data** folder with data (binary data, database templates, etc.)
  9. optionally a **Pipfile** to replace *requirements.txt*

After creating and populating a new GitHub respository (see above), you have to create the *Codecov*
and *Travis* hooks. To do so, sign into *Travis*, click **Profile -> Settings -> Manage Repositories on Github** and follow the instructions from there (install *Travis* for the new or all repositories). For
*Codecov*, once you have linked the coverage service with your GitHub, the coverage report upload as
demonstrated in this repository should work.

----
ToDo
----

  1. Include a Python *contract* module like `dpcontracts <https://github.com/deadpixi/contracts>`_)
  2. Make project pip-installable with *setuptools* (do we need *wheels*?)
  3. Package project with *Docker*
  4. Publish documentation on *readthedocs*?
  5. After next *NumPy* release: make most recent *NumPy* version mandatory such that
     library stubs are available by default
