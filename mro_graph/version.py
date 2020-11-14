#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Version Module

Uses SCM versioning to actually import the version
"""

try:
    from mro_graph.scm_version import version

    version_info = version
except ImportError as e:
    print("Could not import scm version:", e)
    raise ImportError
