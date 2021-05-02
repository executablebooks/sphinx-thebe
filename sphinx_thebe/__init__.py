"""A sphinx extension to enable interactive computations using thebe."""

import json
import os
from pathlib import Path

from docutils.parsers.rst import Directive, directives
from docutils import nodes
from sphinx.util import logging

__version__ = "0.0.8"

logger = logging.getLogger(__name__)


def st_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)


def init_thebe_core(app, env):
    if not app.config["thebe_config"]:
        logger.warning("Didn't find `thebe_config` in conf.py, add to use thebe")
        return

    # Add core libraries
    opts = {"async": "async"}
    app.add_js_file(filename=app.config.thebe_url, **opts)

    # Add configuration variables
    selector_config = f"""
        const thebe_selector = "{ app.config.thebe_selector['cell'] }"
        const thebe_selector_input = "{ app.config.thebe_selector['input'] }"
        const thebe_selector_output = "{ app.config.thebe_selector['output'] }"
    """
    app.add_js_file(None, body=selector_config)
    app.add_js_file(filename="sphinx-thebe.js", **opts)


def update_thebe_context(app, doctree, docname):
    """Add thebe config nodes to this doctree."""
    config_thebe = app.config["thebe_config"]
    if not config_thebe:
        return

    # Thebe configuration
    if config_thebe is True:
        config_thebe = {}
    if not isinstance(config_thebe, dict):
        raise ValueError(
            "thebe configuration must be `True` or a dictionary for configuration."
        )

    # Thebe configuration
    # Choose the kernel we'll use
    meta = app.env.metadata.get(docname, {})
    kernel_name = meta.get("thebe-kernel")
    if kernel_name is None:
        if meta.get("kernelspec"):
            kernel_name = json.loads(meta["kernelspec"]).get("name")
        else:
            kernel_name = "python3"

    # Update the doctree with some nodes for the thebe configuration
    thebe_html_config = f"""
    <script type="text/x-thebe-config">
    { json.dumps(thebe_config) }
    </script>
    """

    doctree.append(nodes.raw(text=thebe_html_config, format="html"))
    doctree.append(
        nodes.raw(text=f"<script>kernelName = '{kernel_name}'</script>", format="html")
    )


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

    # Include Thebe core docs
    app.connect("doctree-resolved", update_thebe_context)
    app.connect("env-updated", init_thebe_core)

    # configuration for this tool
    app.add_config_value("thebe_config", None, "html")
    app.add_config_value(
        "thebe_selector",
        {
            "cell": ".thebe",
            "input": "pre",
            "output": ".output",
        },
        "html",
    )
    app.add_config_value(
        "thebe_url",
        "https://unpkg.com/thebe@0.6.0/lib/index.js",
        "html"
    )

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
