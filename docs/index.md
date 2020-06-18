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

There are two steps to using `sphinx-thebelab`. First, you must mark certain
parts of your page as "ready for thebelab". Next, you must insert a button onto
the page to tell Thebelab to initialize.

### Mark elements for thebelab

By default, thebelab will be run on any elements in your documentation that contain
the class `thebelab` and that have a `<pre`> element underneath them.

You can add code blocks like so:

````
```{code-block}
:class: thebelab
```
````

By default, `sphinx-thebelab` will look for any HTML `<pre>` element *inside* the code
block. Thebelab will run on that element.

### Add an activate button to your page

Next, insert an "activate" button in your documentation with the following
directive:

````
```{thebelab-button}
```
````

Clicking this button will activate Thebelab on the page. If you'd like to manually
add your own button (e.g. with your own extension or theme), see [](add-custom-button).

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
