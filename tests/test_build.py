from bs4 import BeautifulSoup
from pathlib import Path
from subprocess import run
from shutil import copytree, rmtree
import pytest


path_tests = Path(__file__).parent.resolve()
path_docs = path_tests.joinpath("..", "docs")


@pytest.fixture(scope="session")
def sphinx_build(tmpdir_factory):
    class SphinxBuild:
        path_tmp = Path(tmpdir_factory.mktemp("build"))
        path_tmp_docs = path_tmp.joinpath("docs")
        path_build = path_tmp_docs.joinpath("_build")
        path_html = path_build.joinpath("html")
        path_pg_index = path_html.joinpath("index.html")
        path_pg_config = path_html.joinpath("configure.html")
        path_pg_chglg = path_html.joinpath("changelog.html")
        cmd_base = ["sphinx-build", ".", "_build/html", "-a", "-W"]

        def copy(self, path=None):
            """Copy the specified book to our tests folder for building."""
            if path is None:
                path = path_docs
            if not self.path_tmp_docs.exists():
                copytree(path, self.path_tmp_docs)

        def build(self, cmd=None):
            """Build the test book"""
            cmd = [] if cmd is None else cmd
            run(self.cmd_base + cmd, cwd=self.path_tmp_docs, check=True)

        def clean(self):
            """Clean the _build folder so files don't clash with new tests."""
            rmtree(self.path_build)

    return SphinxBuild()


def test_sphinx_thebe(file_regression, sphinx_build):
    """Test building with thebe."""
    sphinx_build.copy()

    # Basic build with defaults
    sphinx_build.build()

    # Testing index for base config
    soup_ix = BeautifulSoup(Path(sphinx_build.path_pg_index).read_text(), "html.parser")
    config = soup_ix("script", {"type": "text/x-thebe-config"})
    assert len(config) == 1
    config = config[0]
    file_regression.check(config.prettify(), basename="config_index", extension=".html")

    # Testing the configure page which has a custom kernel
    soup_conf = BeautifulSoup(
        Path(sphinx_build.path_pg_config).read_text(), "html.parser"
    )
    config = soup_conf("script", {"type": "text/x-thebe-config"})
    assert len(config) == 1
    config = config[0]
    file_regression.check(
        config.prettify(), basename="config_custom", extension=".html"
    )

    # Test launch buttons for custom text and structure
    launch_buttons = soup_conf.select(".thebe-launch-button")
    lb_text = "\n\n".join([ii.prettify() for ii in launch_buttons])
    file_regression.check(lb_text, basename="launch_buttons", extension=".html")

    # Changelog has no thebe button directive, but should have the JS anyway
    soup_chlg = BeautifulSoup(Path(sphinx_build.path_pg_chglg).read_text(), "html.parser")
    assert "https://unpkg.com/thebe" in soup_chlg.prettify()


def test_always_load(file_regression, sphinx_build):
    """Test building with thebe."""
    sphinx_build.copy()

    # Basic build with defaults
    sphinx_build.build(cmd=["-D", "thebe_config.always_load=false"])

    # Thebe should be loaded on a page *with* the directive and not on pages w/o it
    soup_ix = BeautifulSoup(Path(sphinx_build.path_pg_index).read_text(), "html.parser")
    assert "https://unpkg.com/thebe" in soup_ix.prettify()
    # Changelog has no thebe button directive, so shouldn't have JS
    soup_chlg = BeautifulSoup(Path(sphinx_build.path_pg_chglg).read_text(), "html.parser")
    assert "https://unpkg.com/thebe" not in soup_chlg.prettify()
