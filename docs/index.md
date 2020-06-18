# sphinx-thebelab


```{image} https://readthedocs.org/projects/sphinx-thebelab/badge/?version=latest
:target: https://sphinx-thebelab.readthedocs.io/en/latest/?badge=latest
:alt: Documentation
```

```{image} https://img.shields.io/pypi/v/sphinx-thebelab.svg
:target: https://pypi.org/project/sphinx_thebelab
:alt: PyPi page
```

Integrate thebelab into your documentation to make your code cells interactive.

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

## Use

To use `sphinx-thebelab`, include code blocks in your documentation that contain
the class `thebelab`. You can add code blocks like so:

````
```{code-block}
:class: thebelab
```
````

Next, insert an "activate" button in your documentation with the following
directive:

````
```{thebelab-button}
```
````

## Example

The following example shows this functionality with a Python kernel:

```{thebelab-button}
```

```{code-block}
:class: thebelab

print("hi")
```

For more information about how to configure `sphinx-thebelab`, see [](configure.md)

```{toctree}
:hidden:
configure
```
