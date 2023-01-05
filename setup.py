import os
from pathlib import Path

from setuptools import setup, find_packages

with open("./README.md", "r") as ff:
    readme_text = ff.read()

# Parse version
init = Path(__file__).parent.joinpath("sphinx_thebe", "__init__.py")
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        break
version = line.split(" = ")[-1].strip('"')

setup(
    name="sphinx-thebe",
    version=version,
    description="Integrate interactive code blocks into your documentation with Thebe and Binder.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Executable Book Project",
    url="https://github.com/executablebooks/sphinx-thebe",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "sphinx_thebe": [
            "_static/sphinx-thebe.css",
            "_static/sphinx-thebe.js",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["sphinx>=4,<7"],
    extras_require={
        "sphinx": [
            "matplotlib",
            "myst-nb",
            "sphinx-book-theme>=0.4.0rc1",
            "sphinx-copybutton",
            "sphinx-design",
        ],
        "testing": ["matplotlib", "pytest", "pytest-regressions", "beautifulsoup4"],
    },
)
