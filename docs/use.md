# Use `sphinx-thebe`

`sphinx-thebe` uses remote Jupyter kernels to execute your page's code and return the
results, and [Binder](https://mybinder.org) to run the infrastructure for execution.
You can do nearly anything with `sphinx-thebe` that you could do from within a Jupyter Notebook cell.

## Get started

There are two steps to using `sphinx-thebe`. First, you must mark certain
parts of your page as "ready for thebe". Next, you must insert a button onto
the page to tell Thebe to initialize.

### Mark elements for thebe

By default, thebe will be run on any elements in your documentation that contain
the class `thebe` and that have a `<pre`> element underneath them.

You can add code blocks like so:

````
```{code-block} python
:class: thebe
print("hello world!")
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

### An example

Here is what it looks like when you add the two snippets above in one example:

First the code block:

```{code-block} python
:class: thebe
print("hello world!")
```

And now the Thebe button:

```{thebe-button}
```

Clicking this button will activate Thebe on the page.
If you'd like to manually add your own button (e.g. with your own extension or theme), see [](add-custom-button).

### Customize your environment

By default, `sphinx-thebe` will serve the Binder environment for the
[jupyter-stacks-datascience repository](https://github.com/binder-examples/jupyter-stacks-datascience).
See [](configure.md) for information on choosing your own environment.

## A few examples

For example, click the button below (if you have not already clicked the button at the top of the page) and see the sections underneath to watch `sphinx-thebe` in action:

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

## Structure of a `thebe` cell

`sphinx-thebe` can work with two basic code cell structures:

1. **A single code cell**. In this case, there is just a single code cell that has content that should be made executable, like so:
   
   ```html
   <div class="highlight">
       <pre>print("hi!")</pre>
    </div>
    ```
2. **An input/output cell**. Jupyter tools define code cells as a combination of inputs and outputs.
   For example:

   ```html
   <div class="cell">
     <div class="cell_input">
       <pre>print("hi!")</pre>
     </div>
     <div class="cell_output">
       ...outputs here...
     </div>
   </div>
   ```

   In this case, `sphinx-thebe` will treat the `cell_output` in a special fashion, so that it is cleared when you first run its corresponding input code.


(use:selectors)=
## Selectors `sphinx-thebe` looks for by default

By default `sphinx-thebe` will look for two types of code blocks to turn into interactive cells:

- Cells that match a custom class you can add manually.
  It will match:
  - Whole cells: match `.thebe`
  - Cell inputs: match `pre`
  - Cell outputs: match `.output`
- Cells that match [MyST-NB code cells](https://myst-nb.readthedocs.io/).
  It will match:
  - Whole cells: match `.cell`
  - Cell inputs: match `.cell_input`
  - Cell outputs: match `.cell_output`

To customize the selectors that `sphinx-thebe` looks for, see [](configure:selector).

## Interactive outputs

Interactive outputs work with `sphinx-thebe` **if their web dependencies are loaded**.

Many interactive libraries assume that some javascript packages are pre-loaded in a notebook environment. For example, both Jupyter Lab and Notebook come bundled with `require.js`. To use visualization libraries that depend on this, **you must load these libraries on your own in Sphinx**. To do so, you can add the following to your `conf.py`:

```python
def setup(app):
    app.add_js_file("url-of-package.js")
```

Note that some visualization libraries output *bundles of JavaScript/HTML* that will work out-of-the-box. You should consult the documentation of the library you wish to use in order to figure out how to configure it properly. See [the `thebe` examples](https://thebe.readthedocs.io/en/latest/) for examples of some popular visualization libraries.
