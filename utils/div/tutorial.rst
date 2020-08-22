=================================
How to Markup in ReStructuredTest
=================================

.. comments in markdown start with two dots and a space

Introduction
------------

This package is a simple experiment involving the structural layout,
documentation, typing and testing facilities of an actual project like the
resonance related code in `my_sage_repo`.

**Render this .rst with ctrl+shift+r (requires pandoc installed)**
**Alternatively, you can convert this to HTML by using a Sphinx helper routine:**

  ``$ rst2html in_file.rst out_file.html``

.. contents:: Table of Contents
    :depth: 2

=========
Section 1
=========

Here are some examples of what rst (ReStructuredTest) can do: Footnotes are made
like so [1]_ and block quotes are distinguish solely by indentation:

  This is a quote of some very important person

    --important person

Newlines separate paragraphs, additional newlines beyond the first are ignored!
You can also have internal (example_ points to the bold section below) and external
(`Python <http://www.python.org/>`_) hyperlinks.

=========
Section 2
=========

Syntax for so-called ``directives`` like the toc (TableOfContents) above can be
found

.. attention::

	`directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_

They seem useful but for more involved stuff just refer to *LaTeX* :)

Subsection 2.1
--------------

This is just some filler text. Apparently, there is also a way to get automatic
numbering for sections, etc. If you have to write a larger file like that, just
use *LaTeX*!

You can also have citations like [PS]_.

  Next comes the section that the internal hyperlink refers to:

.. _example:

**This is just an example for an internal hyperlink/cross-reference!**



.. [1] https://docutils.sourceforge.io/docs/user/rst/quickref.html#block-quotes
.. [PS] Some Paper by me
