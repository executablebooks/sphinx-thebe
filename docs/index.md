# sphinx-thebe


```{image} https://readthedocs.org/projects/sphinx-thebe/badge/?version=latest
:target: https://sphinx-thebe.readthedocs.io/en/latest/?badge=latest
:alt: Documentation
```

```{image} https://img.shields.io/pypi/v/sphinx-thebe.svg
:target: https://pypi.org/project/sphinx_thebe
:alt: PyPi page
```

Make your code cells interactive with a kernel provided by [Thebe](http://thebelab.readthedocs.org/)
and [Binder](https://mybinder.org).

For example, click the button below. Notice that the code block beneath becomes
editable and runnable!

```{thebe-button} Launch thebe
```

```{code-block} python
:class: thebe

print("hi")
```

See [](use.md) for more information about what you can do with `sphinx-thebe`.

```{note}
This package is a Sphinx wrapper around the excellent [thebe project](http://thebelab.readthedocs.org/),
a javascript tool to convert static code cells into interactive cells backed
by a kernel.
```

## Install

To install `sphinx-thebe` first clonse and install it:

```
pip install sphinx-thebe
```

Then, add it to your Sphinx site's `conf.py` file:

```
extensions = [
    ...
    "sphinx_thebe"
    ...
]
```

## Configure and use

For more information about how to configure `sphinx-thebe`, see [](configure.md).

For more information on using `sphinx-thebe`, see [](use.md).

```{toctree}
:hidden:
use
configure
contribute
examples/rst
```
