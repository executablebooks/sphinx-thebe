"""A small sphinx extension to add "copy" buttons to code blocks."""
import os
from sphinx.util import logging
from docutils.parsers.rst import Directive, directives
from docutils import nodes
import json

from pathlib import Path

__version__ = "0.0.4"

logger = logging.getLogger(__name__)


def st_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)


def init_thebelab_core(app, env):
    config_thebe = app.config["thebe_config"]
    if not config_thebe:
        logger.warning("Didn't find `thebe_config` in conf.py, add to use thebelab")
        return

    # Add core libraries
    opts = {"async": "async"}
    app.add_js_file(filename="https://unpkg.com/thebelab@latest/lib/index.js", **opts)

    # Add configuration variables
    thebe_selector = app.config.thebe_config.get("selector", ".thebe")
    thebe_selector_input = app.config.thebe_config.get("selector_input", "pre")
    thebe_selector_output = app.config.thebe_config.get("selector_output", ".output")
    thebe_config = f"""
        const thebe_selector = "{ thebe_selector }"
        const thebe_selector_input = "{ thebe_selector_input }"
        const thebe_selector_output = "{ thebe_selector_output }"
    """
    app.add_js_file(None, body=thebe_config)
    app.add_js_file(filename="thebelab.js", **opts)


def update_thebelab_context(app, doctree, docname):
    """Add thebelab config nodes to this doctree."""
    config_thebe = app.config["thebe_config"]
    if not config_thebe:
        return

    # Thebe configuration
    if config_thebe is True:
        config_thebe = {}
    if not isinstance(config_thebe, dict):
        raise ValueError(
            "thebelab configuration must be `True` or a dictionary for configuration."
        )
    codemirror_theme = config_thebe.get("codemirror-theme", "abcdef")

    # Thebelab configuration
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

    # Update the doctree with some nodes for the thebelab configuration
    thebelab_html_config = f"""
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

    doctree.append(nodes.raw(text=thebelab_html_config, format="html"))
    doctree.append(
        nodes.raw(text=f"<script>kernelName = '{kernel_name}'</script>", format="html")
    )


def _split_repo_url(url):
    """Split a repository URL into an org / repo combination."""
    if "github.com/" in url:
        end = url.split("github.com/")[-1]
        org, repo = end.split("/")[:2]
    else:
        logger.warning(f"Currently Thebelab repositories must be on GitHub, got {url}")
        org = repo = None
    return org, repo


class ThebeLabButtonNode(nodes.Element):
    """Appended to the doctree by the ThebeButton directive

    Renders as a button to enable thebelab on the page.

    If no ThebeButton directive is found in the document but thebelab
    is enabled, the node is added at the bottom of the document.
    """

    def __init__(self, rawsource="", *children, text="Run code", **attributes):
        super().__init__("", text=text)

    def html(self):
        text = self["text"]
        return (
            '<button title="{text}" class="thebelab-button thebe-launch-button"'
            'onclick="initThebelab()">{text}</button>'.format(text=text)
        )


class ThebeLabButton(Directive):
    """Specify a button to activate thebelab on the page

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
        return [ThebeLabButtonNode(**kwargs)]


# Used to render an element node as HTML
def visit_element_html(self, node):
    self.body.append(node.html())
    raise nodes.SkipNode


# Used for nodes that do not need to be rendered
def skip(self, node):
    raise docutils.nodes.SkipNode


def setup(app):
    logger.verbose("Adding copy buttons to code blocks...")
    # Add our static path
    app.connect("builder-inited", st_static_path)

    # configuration for this tool
    app.add_config_value("thebe_config", {}, "html")

    # Include Thebelab core docs
    app.connect("doctree-resolved", update_thebelab_context)
    app.connect("env-updated", init_thebelab_core)

    app.add_directive("thebe-button", ThebeLabButton)

    # Add relevant code to headers
    app.add_css_file("thebelab.css")

    # ThebeLabButtonNode is the button that activates thebelab
    # and is only rendered for the HTML builder
    app.add_node(
        ThebeLabButtonNode,
        html=(visit_element_html, None),
        latex=(skip, None),
        textinfo=(skip, None),
        text=(skip, None),
        man=(skip, None),
    )

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
