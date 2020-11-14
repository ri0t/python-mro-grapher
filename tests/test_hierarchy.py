#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
Draw inheritance hierarchies via Dot (http://www.graphviz.org/)
Author: Michele Simionato (and Heiko 'riot' Weinen)
E-mail: mis6@pitt.edu
Date: August 2003, 2020
License: Python-like
Requires: Python 2.3, dot, standard Unix tools
"""

from mro_graph import MROGraph


def testHierarchy(**options):
    class M(type):
        pass  # metaclass

    class F(object):
        pass

    class E(object):
        pass

    class D(object):
        pass

    class G(object):
        __metaclass__ = M

    class C(F, D, G):
        pass

    class B(E, D):
        pass

    class A(B, C):
        pass

    return MROGraph(A, M, **options)


if __name__ == "__main__":
    testHierarchy()  # generates a postscript diagram of A and M hierarchies
