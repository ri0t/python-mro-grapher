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

from mro_graph import MROGraph


def test_hierarchy(**options):
    class M(type):
        pass  # metaclass

    class F(object):
        pass

    class E(object):
        pass

    class D(object):
        pass

    class G(object):
        # noinspection PyUnusedName
        __metaclass__ = M

    class C(F, D, G):
        pass

    class B(E, D, M):
        pass

    class A(B, C):
        pass

    return MROGraph(A, M, **options)
