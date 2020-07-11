================
Using rST syntax
================

This documentation is written in `MyST Markdown <https://myst-parser.readthedocs.io/>`_,
so the syntax shown is a little bit different than many Sphinx sites, which are written
in reStructuredText. However, ``sphinx-thebe`` works fine in both. Here is the syntax
for using ``sphinx-thebe`` with rST:

Adding a ``thebe`` class to a code block:

.. code-block:: python
   :class: thebe

   print("hi!")

And adding a button:

.. thebe-button:: Click me!
