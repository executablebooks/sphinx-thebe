# Contributing to Sphinx-Thebe

Thanks for your interest in contributing to `sphinx-thebe`, your contributions are welcome and appreciated 🎉. This page contains some information to help you get started.

## Contributing guide

See the [ExecutableBooks developer guidelines](https://executablebooks.org/en/latest/contributing.html) for conventions and practices around developing `sphinx-thebe`.


## Repository structure

`sphinx-thebe` is a lightweight extensions for Sphinx to activate and configure the [thebe javascript package](https://thebe.readthedocs.io/en/latest/). Most of the heavy lifting is done by that package, while this package mostly just integrates it with Sphinx and provides a button that can activate `thebe` under the hood.

- The sphinx package is contained in `sphinx_thebe/`. The `__init__.py` file contains the code that activates and loads the proper CSS and JS when Sphinx is run.
- CSS and Javascript assets are in `sphinx_thebe/_static`. These handle the activation of `thebe` on a page via a button-click, and also make minor modification to the page's DOM to make it work well with `thebe`.

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