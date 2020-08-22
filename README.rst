================================
How to Package A Python3 Project
================================

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

    1. The __init__.py contains any code
       that should be executed whenever a module is imported.

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

We will also implement code coverage using
`Codecov <https://docs.codecov.io/docs/quick-start>`_.

----
ToDo
----

  0. Install all needed packages, etc. with *Pipenv*! Also, populate Makefile
  1. Create some dummy code
  2. Initialize and build documentation, add description here
  3. Create stubs for custom classes and functions
  4. Choose a testing module and create tests (maybe include some Python
     *contract* module like `dpcontracts <https://github.com/deadpixi/contracts>`_)
  5. Implement continuous integration with Travis CI, implement coverage reports
     with `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/reporting.html>`_
     and codecov
  6. Make project pip-installable with *wheels* (and *setuptools*?)
  7. Package project with *Docker*
