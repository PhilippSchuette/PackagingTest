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

  ``$ sphinx-quickstart``

----------
MyPy Stubs
----------

The stubs used for `MyPy <https://mypy.readthedocs.io/en/stable/>`_ static type
checking are contained within the subdirectory *stubs/*. You have to add this
directory to your ``MYPYPATH`` for type checking to work (or enable the correct
setting in an editor like atom).

-------
Testing
-------

We will probably want to use `PyTest <https://docs.pytest.org/en/stable/contents.html>`_
together with `Hypothesis <https://hypothesis.readthedocs.io/en/latest/quickstart.html>`_
to implement so-called *property testing*.

We will also implement code coverage using
`Codecov <https://docs.codecov.io/docs/quick-start>`_.

----
ToDo
----

  0. Install all needed packages, etc. with *Pipenv*! Also, populate Makefile,
     CODE_OF_CONDUCT, LICENSE, CONTRIBUTING
  1. Create some dummy code
  2. Initialize and build documentation, add description here
  3. Create stubs for custom classes and functions
  4. Choose a testing module and create tests (maybe include some Python
     *contract* module like `dpcontracts <https://github.com/deadpixi/contracts>`_)
  5. Implement continuous integration with Travis CI, implement coverage reports
     with `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/reporting.html>`_
     and codecov
  6. Make project pip-installable
  7. Package project with *Docker*
