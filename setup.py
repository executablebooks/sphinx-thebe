import os
from pathlib import Path

from setuptools import setup, find_packages

with open("./README.md", "r") as ff:
    readme_text = ff.read()

# Parse version
init = Path(__file__).parent.joinpath("sphinx_thebelab", "__init__.py")
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        break
version = line.split(" = ")[-1].strip('"')

setup(
    name="sphinx-thebelab",
    version=version,
    description="Add a copy button to each of your code cells.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Executable Book Project",
    url="https://github.com/executablebooks/sphinx-thebelab",
    license="MIT License",
    packages=find_packages(),
    package_data={
        "sphinx_thebelab": [
            "_static/thebelab.css",
            "_static/thebelab.js",
        ]
    },
    classifiers=["License :: OSI Approved :: MIT License"],
    install_requires=["sphinx>=1.8"],
    extras_require={"sphinx": ["myst-parser[sphinx]"], "testing": ["pytest", "pytest-regressions", "beautifulsoup4"]},
)
