#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="mro-graph",
    description="A small tool to generate and illustrate (via dot) the method "
                "resolution order graph of Python objects ",
    author="Michele Simionato ",
    author_email="mis6@pitt.edu",
    maintainer="Heiko 'riot' Weinen",
    maintainer_email="riot@c-base.org",
    project_urls={
        "Download": "https://github.com/ri0t/python-mro-grapher/releases",
        "Source": "https://github.com/ri0t/python-mro-grapher",
        "Tracker": "https://github.com/ri0t/python-mro-grapher/issues",
    },
    license="Python-like",  # ?!? PSF-License?
    keywords="developer-tools mro python2 python3 method resolution order dot "
             "visualizer tool graph",
    classifiers=[
        "Development Status :: 4 - Beta",  # Hmm.
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=[
        "mro_graph",
    ],
    long_description=readme,
    long_description_content_type="text/x-rst",
    entry_points="""[console_scripts]
    mro-graph=mro_graph.mro_graph:main
    """,
    install_requires=[
        "click>=7.1.2"
    ],
    use_scm_version={
        "write_to": "mro_graph/scm_version.py",
    },
    setup_requires=["setuptools_scm"],
    test_suite="tests.main.main",
)
