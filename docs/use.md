# Using `sphinx-thebe`

## Get started

There are two steps to using `sphinx-thebe`. First, you must mark certain
parts of your page as "ready for thebe". Next, you must insert a button onto
the page to tell Thebe to initialize.

:::{admonition} Using reStructuredText vs. MyST Markdown
:class: tip
The examples on this page use **MyST Markdown syntax**, a form of markdown that works with Sphinx directives. You can also use reStructuredText if you wish. For information about reStructuredText vs. MyST Markdown, see [the MyST Parser documentation](https://myst-parser.readthedocs.io/en/latest/using/syntax.html) as well as [](examples/rst) for some tips.
:::

### Mark elements for thebe

By default, thebe will be run on any elements in your documentation that contain
the class `thebe` and that have a `<pre`> element underneath them.

You can add code blocks like so:

````
```{code-block}
:class: thebe
```
````

By default, `sphinx-thebe` will look for any HTML `<pre>` element *inside* the code
block. Thebe will run on that element.

### Add an activate button to your page

Next, insert an "activate" button in your documentation with the following
directive:

````
```{thebe-button}
```
````

The button looks like this:

```{thebe-button}
```

Clicking this button will activate Thebe on the page. If you'd like to manually
add your own button (e.g. with your own extension or theme), see [](add-custom-button).

```{note}
By default, `sphinx-thebe` will serve the Binder environment for the
[jupyter-stacks-datascience repository](https://github.com/binder-examples/jupyter-stacks-datascience).
See [](configure.md) for information on choosing your own environment.
```

## What can I do with `sphinx-thebe`?

`sphinx-thebe` uses Jupyter kernels to execute your page's code and return the
results, and Binder in order to run the infrastructure for execution. This means that
you can do nearly anything with `sphinx-thebe` that you could do from within a
Jupyter Notebook cell.

```{admonition} You can customize your environment
:class: tip

You can customize the environment that powers your interactive code sessions using
a Binder repository. This may allow for different kinds of functionality depending on
the libraries that are installed. See [](configure.md) for more information.
```

For example:

```{thebe-button} Launch examples below!
```

### Code outputs

```{code-block}
:class: thebe, thebe-init

import numpy as np
np.random.seed(1337)
data = np.random.randn(2, 100)
print(data[1, :10])
```

### DataFrames

```{code-block}
:class: thebe

import pandas as pd
df = pd.DataFrame(data.T, columns=["a", "b"])
df.head(5)
```

### PNG outputs

```{code-block}
:class: thebe
import matplotlib.pyplot as plt
plt.scatter(*data, c=data[0], s=200)
```

## Interactive outputs

Interactive outputs work with `sphinx-thebe` **if their web dependencies are loaded**.

Many interactive libraries assume that some javascript packages are pre-loaded in a notebook environment. For example, both Jupyter Lab and Notebook come bundled with `require.js`. To use visualization libraries that depend on this, **you must load these libraries on your own in Sphinx**. To do so, you can add the following to your `conf.py`:

```python
def setup(app):
    app.add_js_file("url-of-package.js")
```

Note that some visualization libraries output *bundles of JavaScript/HTML* that will work out-of-the-box. You should consult the documentation of the library you wish to use in order to figure out how to configure it properly. See [the `thebe` examples](https://thebe.readthedocs.io/en/latest/) for examples of some popular visualization libraries.
