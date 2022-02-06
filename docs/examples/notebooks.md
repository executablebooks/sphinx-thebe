---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Jupyter Notebooks

This page was written for [MyST-NB](https://myst-nb.readthedocs.io/).
It demonstrates `sphinx-thebe`'s usage with Jupyter Notebooks.

Activate Thebe by clicking the launch button below.
You should then be able to run and edit the code cell in the notebook.

```{thebe-button} Launch thebe
```

The outputs should be displayed below, but they will be collected by `sphinx-thebe` when it is activated so that they are cleared when you first run the cell.

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt

# Create some fake data
data = np.random.randn(3, 1000)

# Create a figure
fig, ax = plt.subplots()

# Plot data
ax.scatter(data[0], data[1], c=np.abs(data[2]), s=np.abs(data[2])*100)
```

## Code style

Thebe uses CodeMirror in the background, which uses different styles than pygments, which is used for static code syntax highlighting.

The below code block is **static** and will not be converted with `thebe`.
We include it in order to compare the active Thebe cell's syntax highlighting with an inactive cell.

```
import numpy as np
import matplotlib.pyplot as plt

# Create some fake data
data = np.random.randn(3, 1000)

# Create a figure
fig, ax = plt.subplots()

# Plot data
ax.scatter(data[0], data[1], c=np.abs(data[2]), s=np.abs(data[2])*100)
```
