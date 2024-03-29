# Contribute to `sphinx-thebe`

Thanks for your interest in contributing to `sphinx-thebe`, your contributions are welcome and appreciated 🎉. This page contains some information to help you get started.

## Design philosophy

`sphinx-thebe` is designed to be a simple bridge between Sphinx and `thebe`.
It should not add a lot of extra functionality on top of Thebe, beyond special-casing its configuration for Sphinx objects and its build system.
It's primary goal is to make it pain-free to load `thebe.js` and apply it to websites generated by Sphinx with reasonable default choices.

`sphinx-thebe` adds default configuration to support major Jupyter Notebook extensions in the Sphinx ecosystem.
Currently this means [MyST-NB](https://myst-nb.readthedocs.io/), but in the future we'd also like to support [nbsphinx](https://nbsphinx.readthedocs.io/) by default.

## Contributing guide

See the [ExecutableBooks developer guidelines](https://executablebooks.org/en/latest/contributing.html) for conventions and practices around developing `sphinx-thebe`.


## Repository structure

`sphinx-thebe` is a lightweight extensions for Sphinx to activate and configure the [thebe javascript package](https://thebe.readthedocs.io/en/latest/). Most of the heavy lifting is done by that package, while this package mostly just integrates it with Sphinx and provides a button that can activate `thebe` under the hood.

- The sphinx package is contained in `sphinx_thebe/`. The `__init__.py` file contains the code that activates and loads the proper CSS and JS when Sphinx is run.
- CSS and Javascript assets are in `sphinx_thebe/_static`. These handle the activation of `thebe` on a page via a button-click, and also make minor modification to the page's DOM to make it work well with `thebe`.

## Code style

The JavaScript and CSS assets for this repository follow the default values for [prettier](https://prettier.io/).

Python code follows `black` and `pep8` as described in [the EBP contributing guide](https://executablebooks.org/en/latest/contributing.html#coding-style).


## Installation for development

To install `sphinx-thebe` for development clone and install `sphinx-thebe` locally:

```bash
git clone https://github.com/executablebooks/sphinx-thebe
cd sphinx-thebe
pip install -e .[sphinx,testing]
```

When you build Sphinx documentation with `sphinx-thebe` activated, it should now use the local development version. You can try this by building the `sphin-thebe` documentation:

```bash
cd docs
make html
```