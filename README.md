# sphinx-thebelab

[![PyPI](https://img.shields.io/pypi/v/sphinx-thebelab.svg)](https://pypi.org/project/sphinx_thebelab/) | [![Documentation](https://readthedocs.org/projects/sphinx-thebelab/badge/?version=latest)](https://sphinx-thebelab.readthedocs.io/en/latest/?badge=latest)

A small sphinx extension to add a "copy" button to code blocks.

See [the sphinx-thebelab documentation](https://sphinx-thebelab.readthedocs.io/en/latest/) for more details!

![](doc/_static/copybutton.gif)

## Installation

You can install `sphinx-thebelab` with `pip`:

```
pip install sphinx-thebelab
```

## Usage

In your `conf.py` configuration file, add `sphinx_thebelab` to your extensions list.
E.g.:

```
extensions = [
    ...
    'sphinx_thebelab'
    ...
]
```

When you build your site, your code blocks should now have little copy buttons to their
right. Clicking the button will copy the code inside!

## Customization

If you'd like to customize the look of the copy buttons, you can over-write any of the
CSS rules specified in the sphinx-thebelab CSS file ([link](sphinx_thebelab/_static/copybutton.css))
