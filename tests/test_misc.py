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
Test general functionality
"""

import os
from mro_graph import MROGraph

dict_mro_str = """MRO of dict:
  0 - dict(object)
  1 - object()"""

dict_mro_repr = """digraph MRO_of_dict{
 node [fontname=Times];
 edge [fontname=Times];


 edge [style=solid]; object -> dict ;

 dict [shape=box,label="0-dict"];

 object [shape=box,label="1-object"];
}"""

dict_mro_dot = """digraph test{
 node [];
 edge [];


 edge [style=solid]; object -> dict ;

 dict [shape=box,label="0-dict"];

 object [shape=box,label="1-object"];
}"""


def test_repr(**options):
    mro_object = MROGraph(dict, **options)

    assert repr(mro_object) == dict_mro_repr


def test_str(**options):
    mro_object = MROGraph(dict, **options)

    assert str(mro_object) == dict_mro_str


def test_dot_export(**options):
    options["filename"] = "test.dot"
    _ = MROGraph(dict, **options)

    assert os.path.exists("test.dot")

    with open("test.dot", "r") as f:
        assert f.read() == dict_mro_dot


def test_scm_version():
    from mro_graph.version import version as static_version
    from mro_graph.scm_version import version as scm_version

    assert static_version is not None
    assert scm_version is not None
