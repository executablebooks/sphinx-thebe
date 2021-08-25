"""A sphinx extension to enable interactive computations using thebe."""

import json
import os
from pathlib import Path

from docutils.parsers.rst import Directive, directives
from docutils import nodes
from sphinx.util import logging

__version__ = "0.0.10"

logger = logging.getLogger(__name__)

THEBE_VERSION = "0.5.1"


def st_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)


def init_thebe_default_config(app, env, docnames):
    thebe_config = app.config.thebe_config
    defaults = {
        "always_load": True,
        "selector": ".thebe",
        "selector_input": "pre",
        "selector_output": ".output",
    }
    for key, val in defaults.items():
        if key not in thebe_config:
            thebe_config[key] = val


def _bool(b):
    if isinstance(b, bool):
        return b
    else:
        return b in ["true", "True"]


def _do_load_thebe(doctree, config_thebe):
    """Decide whether to load thebe based on the page's context."""
    if not doctree:
        return False

    # If we aren't properly configured
    if not config_thebe:
        logger.warning("Didn't find `thebe_config` in conf.py, add to use thebe")
        return False

    # Only load `thebe` if there is a thebe button somewhere
    if doctree.traverse(ThebeButtonNode) or _bool(config_thebe.get("always_load")):
        return True
    else:
        return False


def init_thebe_core(app, pagename, templatename, context, doctree):
    """Load thebe assets if there's a thebe button on this page."""
    config_thebe = app.config["thebe_config"]
    if not _do_load_thebe(doctree, config_thebe):
        return

    # Add core libraries
    opts = {"async": "async"}
    app.add_js_file(
        filename=f"https://unpkg.com/thebe@{THEBE_VERSION}/lib/index.js", **opts
    )

    # Add configuration variables
    thebe_config = f"""
        const thebe_selector = "{ app.config.thebe_config['selector'] }"
        const thebe_selector_input = "{ app.config.thebe_config['selector_input'] }"
        const thebe_selector_output = "{ app.config.thebe_config['selector_output'] }"
    """
    app.add_js_file(None, body=thebe_config)
    app.add_js_file(filename="sphinx-thebe.js", **opts)


def update_thebe_context(app, doctree, docname):
    """Add thebe config nodes to this doctree."""
    config_thebe = app.config["thebe_config"]
    if not _do_load_thebe(doctree, config_thebe):
        return

    # Thebe configuration
    if config_thebe is True:
        config_thebe = {}
    if not isinstance(config_thebe, dict):
        raise ValueError(
            "thebe configuration must be `True` or a dictionary for configuration."
        )
    codemirror_theme = config_thebe.get("codemirror-theme", "abcdef")

    # Thebe configuration
    # Choose the kernel we'll use
    meta = app.env.metadata.get(docname, {})
    kernel_name = meta.get("thebe-kernel")
    if kernel_name is None:
        if meta.get("kernelspec"):
            kernel_name = json.loads(meta["kernelspec"]).get("name")
        else:
            kernel_name = "python3"

    # Codemirror syntax
    cm_language = kernel_name
    if "python" in cm_language:
        cm_language = "python"
    elif cm_language == "ir":
        cm_language = "r"

    # Create the URL for the kernel request
    repo_url = config_thebe.get(
        "repository_url",
        "https://github.com/binder-examples/jupyter-stacks-datascience",
    )
    branch = config_thebe.get("repository_branch", "master")
    path_to_docs = config_thebe.get("path_to_docs", ".").strip("/") + "/"
    org, repo = _split_repo_url(repo_url)

    # Update the doctree with some nodes for the thebe configuration
    thebe_html_config = f"""
    <script type="text/x-thebe-config">
    {{
        requestKernel: true,
        binderOptions: {{
            repo: "{org}/{repo}",
            ref: "{branch}",
        }},
        codeMirrorConfig: {{
            theme: "{codemirror_theme}",
            mode: "{cm_language}"
        }},
        kernelOptions: {{
            kernelName: "{kernel_name}",
            path: "{path_to_docs}{str(Path(docname).parent)}"
        }},
        predefinedOutput: true
    }}
    </script>
    """

    doctree.append(nodes.raw(text=thebe_html_config, format="html"))
    doctree.append(
        nodes.raw(text=f"<script>kernelName = '{kernel_name}'</script>", format="html")
    )


def _split_repo_url(url):
    """Split a repository URL into an org / repo combination."""
    if "github.com/" in url:
        end = url.split("github.com/")[-1]
        org, repo = end.split("/")[:2]
    else:
        logger.warning(f"Currently Thebe repositories must be on GitHub, got {url}")
        org = repo = None
    return org, repo


class ThebeButtonNode(nodes.Element):
    """Appended to the doctree by the ThebeButton directive

    Renders as a button to enable thebe on the page.

    If no ThebeButton directive is found in the document but thebe
    is enabled, the node is added at the bottom of the document.
    """

    def __init__(self, rawsource="", *children, text="Run code", **attributes):
        super().__init__("", text=text)

    def html(self):
        text = self["text"]
        return (
            '<button title="{text}" class="thebelab-button thebe-launch-button"'
            'onclick="initThebe()">{text}</button>'.format(text=text)
        )


class ThebeButton(Directive):
    """Specify a button to activate thebe on the page

    Arguments
    ---------
    text : str (optional)
        If provided, the button text to display

    Content
    -------
    None
    """

    optional_arguments = 1
    final_argument_whitespace = True
    has_content = False

    def run(self):
        kwargs = {"text": self.arguments[0]} if self.arguments else {}
        return [ThebeButtonNode(**kwargs)]


# Used to render an element node as HTML
def visit_element_html(self, node):
    self.body.append(node.html())
    raise nodes.SkipNode


# Used for nodes that do not need to be rendered
def skip(self, node):
    raise nodes.SkipNode


def setup(app):
    logger.verbose("Adding copy buttons to code blocks...")
    # Add our static path
    app.connect("builder-inited", st_static_path)

    # Set default values for the configuration
    app.connect("env-before-read-docs", init_thebe_default_config)

    # Update the doctree with thebe-specific information if needed
    app.connect("doctree-resolved", update_thebe_context)

    # Load the JS/CSS assets for thebe if needed
    app.connect("html-page-context", init_thebe_core)

    # configuration for this tool
    app.add_config_value("thebe_config", {}, "html")

    # override=True in case Jupyter Sphinx has already been loaded
    app.add_directive("thebe-button", ThebeButton, override=True)

    # Add relevant code to headers
    app.add_css_file("sphinx-thebe.css")

    # ThebeButtonNode is the button that activates thebe
    # and is only rendered for the HTML builder
    app.add_node(
        ThebeButtonNode,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
        override=True,
    )

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
