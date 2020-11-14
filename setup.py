#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Python MRO-graph generator
# ==========================
# Copyright (C) 2003 Michele Simionato
# Copyright (C) 2019-2020 Heiko 'riot' Weinen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Based upon Michele Simionato's work from 2003:
http://www.phyast.pitt.edu/~micheles/python/drawMRO.html

Notice the - back then - missing ternary operations.
That was so old-school :D
"""

from setuptools import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="mro-graph",
    description="A small tool to generate and illustrate (via dot) the method "
                "resolution order graph of Python objects ",
    author="Michele Simionato",
    author_email="mis6@pitt.edu",
    maintainer="Heiko 'riot' Weinen",
    maintainer_email="riot@c-base.org",
    project_urls={
        "Download": "https://github.com/ri0t/python-mro-graph/releases",
        "Source": "https://github.com/ri0t/python-mro-graph",
        "Tracker": "https://github.com/ri0t/python-mro-graph/issues",
    },
    license="GNU General Public License v3",  # Was: PSF-like, GPL3 is PSF-like
    keywords="developer-tools mro python2 python3 method resolution order dot "
             "visualizer tool graph",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
