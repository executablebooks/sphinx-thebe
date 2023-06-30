project = "Sphinx Thebe"
copyright = "2020, Executable Book Project"
author = "Executable Book Project"
version = ""
release = ""

extensions = [
    "myst_parser",
    "sphinx_thebe",
    "myst_nb",
]

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "path_to_docs": "docs",
}

myst_enable_extensions = ["colon_fence"]
source_suffix = [".rst", ".md"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
