# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys
import re
import json
import urllib.request

from sphinx.errors import SphinxError
from pygments.lexers.data import YamlLexer

sys.path.append(os.path.abspath('_extensions'))


# -- Project information -----------------------------------------------------

project = "Develop with Moreh Documentation"
copyright = "Develop with Moreh Documentation"
author = "johyun an"


# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "hoverxref.extension",
    "sphinx_tabs.tabs",
    "sphinx_rtd_theme",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinxcontrib.httpdomain",
    "myst_parser",
    "sphinx_design",
]

bibtex_bibfiles = ['refs.bib']

intersphinx_mapping = {
    'readthedocs': ('https://docs.readthedocs.io/en/stable/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'sympy': ('https://docs.sympy.org/latest/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'python': ('https://docs.python.org/3/', None),

}


templates_path = ["_templates"]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
hoverxref_intersphinx = [
    "sphinx",
    "readthedocs",
    "python",
    "sympy",
    "numpy",
]


hoverxref_intersphinx_types = {
    'readthedocs': 'modal',
    'sphinx': 'tooltip',
}


# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

sphinx_tabs_valid_builders = ["linkcheck"]



pygments_style = "sphinx"
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"


#html_css_files = ["css/custom.css", "css/sphinx_prompt_css.css"]
#html_js_files = ["js/expand_tabs.js"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

#html_static_path = ["_static"]


# -- Custom Pygments lexers for OpenAPI -----------------------------------


#sphinx_tabs_disable_tab_closing = True

#sphinx_tabs_disable_css_loading = True