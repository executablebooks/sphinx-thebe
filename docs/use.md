# Using `sphinx-thebelab`

## Get started

There are two steps to using `sphinx-thebelab`. First, you must mark certain
parts of your page as "ready for thebelab". Next, you must insert a button onto
the page to tell Thebelab to initialize.

### Mark elements for thebelab

By default, thebelab will be run on any elements in your documentation that contain
the class `thebelab` and that have a `<pre`> element underneath them.

```{note}
This documentation is written in [MyST Markdown](https://myst-parser.readthedocs.io),
so the syntax for writing directives looks different from reStructuredText. However,
rST works just fine as well.
```

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

The button looks like this:

```{thebelab-button}
```

Clicking this button will activate Thebelab on the page. If you'd like to manually
add your own button (e.g. with your own extension or theme), see [](add-custom-button).

```{note}
By default, `sphinx-thebelab` will serve the Binder environment for the
[jupyter-stacks-datascience repository](https://github.com/binder-examples/jupyter-stacks-datascience).
See [](configure.md) for information on choosing your own environment.
```

## What can I do with `sphinx-thebelab`?

`sphinx-thebelab` uses Jupyter kernels to execute your page's code and return the
results, and Binder in order to run the infrastructure for execution. This means that
you can do nearly anything with `sphinx-thebelab` that you could do from within a
Jupyter Notebook cell.

```{admonition} You can customize your environment
:class: tip

You can customize the environment that powers your interactive code sessions using
a Binder repository. This may allow for different kinds of functionality depending on
the libraries that are installed. See [](configure.md) for more information.
```

For example:

```{thebelab-button} Launch examples below!
```

### Code outputs

```{code-block}
:class: thebelab, thebelab-init

import numpy as np
np.random.seed(1337)
data = np.random.randn(2, 100)
print(data[1, :10])
```

### DataFrames

```{code-block}
:class: thebelab

import pandas as pd
df = pd.DataFrame(data.T, columns=["a", "b"])
df.head(5)
```

### PNG outputs

```{code-block}
:class: thebelab
import matplotlib.pyplot as plt
plt.scatter(*data, c=data[0], s=200)
```

### Interactive outputs

Interactive outputs are still a little bit flaky, but please try out
`sphinx-thebelab` with the interactive visualization library of your choice,
and report back how things work!

As a general rule, `sphinx-thebelab` will only work with interactive libraries
that are able to output self-contained bundles of HTML/JS that work on their own.
Many Jupyter environments have libraries pre-loaded, and that will not be the case
with `sphinx-thebelab`.
