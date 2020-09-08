================================
How to Package A Python3 Project
================================

.. image:: https://codecov.io/gh/PhilippSchuette/PackagingTest/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/PhilippSchuette/PackagingTest

.. image:: https://travis-ci.com/PhilippSchuette/PackagingTest.svg?token=Yiib7xzboAJu8y3Dk8Qo&branch=master
   :target: https://travis-ci.com/PhilippSchuette/PackagingTest

.. image:: https://img.shields.io/badge/Language-Python-blue.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/github/v/release/PhilippSchuette/PackagingTest
   :target: https://github.com/PhilippSchuette/PackagingTest

.. image:: https://img.shields.io/badge/docs-docstr--cov-success
   :target: https://pypi.org/project/docstr-coverage/

.. image:: https://img.shields.io/badge/mypy-checked-blue
   :target: https://mypy.readthedocs.io/en/stable/

--------------------------------------------------------------------------------

.. contents:: Table of Contents
  :depth: 2

------------
Introduction
------------

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

Finally, you have to update the release version in the documentation (`docs/conf.py`)
and the `setup.py`. You can embedded badges indicating the recent version as seen above.

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

.. note::
  **index.rst contains examples on how to include LaTeX using the raw directive!**

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

------------------------
Cython Extension Modules
------------------------

**Cython** extension modules provide a convenient way to combine the speed of **C** or
**C++** code with the advantages of pure (C)Python. There are several ways of using
**Cython**, but in this project you can simply type

.. code:: bash

  $ python3 setup.py build_ext --inplace

The current **Travis** build also includes the **Cython** generated *.so* extensions.

----
ToDo
----

  1. Include a Python *contract* module like `dpcontracts <https://github.com/deadpixi/contracts>`_)
  2. Make project pip-installable with *setuptools* (do we need *wheels*?)
  3. Package project with *Docker*
  4. Publish documentation on *readthedocs*?
  5. Create an appropriately packaged example for C extension modules created with
     **`Cython <https://cython.readthedocs.io/en/latest/>`_**
  6. Integrate **Cython** with the rest of the package, i.e. package type hint stubs
     appropriately and without duplication between **Cython** and **MyPy**
