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
import os
import sys
sys.path.insert(0, os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------

project = 'Granite.Code Docs'
copyright = 'Red Hat, Inc.'
author = 'Allan Day'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser"
]

myst_enable_extensions = [
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#4a86cf",
        "color-brand-content": "#4a86cf",
    },
    "sidebar_hide_name": True,
    "source_edit_link": "https://github.com/Granite-Code/docs.granitecode.github.io/edit/main/docs/{filename}",
}
html_favicon = 'img/favicon.svg'
html_logo = "img/logo.svg"

# Set the explicit title of the HTML output
html_title = 'Granite.Code Documentation'

# add custom files that are stored in _static
html_css_files = ['granite.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#footer stuff
html_show_copyright = 0
html_show_sphinx = 0
show_source = 0

