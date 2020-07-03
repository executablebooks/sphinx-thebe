# sphinx-thebelab


```{image} https://readthedocs.org/projects/sphinx-thebelab/badge/?version=latest
:target: https://sphinx-thebelab.readthedocs.io/en/latest/?badge=latest
:alt: Documentation
```

```{image} https://img.shields.io/pypi/v/sphinx-thebelab.svg
:target: https://pypi.org/project/sphinx_thebelab
:alt: PyPi page
```

Make your code cells interactive with a kernel provided by [Thebelab](http://thebelab.readthedocs.org/)
and [Binder](https://mybinder.org).

For example, click the button below. Notice that the code block beneath becomes
editable and runnable!

```{thebe-button} Launch thebelab
```

```{code-block}
:class: thebe

print("hi")
```

See [](use.md) for more information about what you can do with `sphinx-thebelab`.

```{note}
This package is a Sphinx wrapper around the excellent [thebelab project](http://thebelab.readthedocs.org/),
a javascript tool to convert static code cells into interactive cells backed
by a kernel.
```

## Install

To install `sphinx-thebelab` first clonse and install it:

```
git clone https://github.com/executablebooks/sphinx-thebelab
cd sphinx-thebelab
pip install -e .
```

Then, add it to your Sphinx site's `conf.py` file:

```
extensions = [
    ...
    "sphinx_thebelab"
    ...
]
```

## Configure and use

For more information about how to configure `sphinx-thebelab`, see [](configure.md).

For more information on using `sphinx-thebelab`, see [](use.md).

```{toctree}
:hidden:
use
configure
```
