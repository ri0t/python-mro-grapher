python-mro-graph generator
##########################

A small tool to generate and illustrate (via dot) the method resolution order graph of
Python objects

Requirements
============

Generating a graph needs the dot tool installed. Usually this tool resides in the
`graphviz` package.

Additionally - to display the resulting graphs - either imagemagick or ghostview or
some other postscript or png viewer is required.

Usage
=====

Command line tool
-----------------

You will need to be able to import the object you want to investigate.

Simple usage: builtins
~~~~~~~~~~~~~~~~~~~~~~

A simple example demonstrating usage for builtin objects:

.. code-block::

    mro-graph "" "dict"

..which displays the MRO of a simple dictionary. Notice that IMPORT_EXEC
is left empty, that is because we do not need to import anything to inspect
builtins.

Complex usage: packaged objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Say, you have a package called `test` which contains a module called `test_module`
which in turn contains the object you want to inspect, called `test_object`.

To inspect it, call `mro-graph` and instruct it to generate a graph:

.. code-block::

    mro-graph "from test.test_module import test_object" "test_object"

..which should result in it displaying the MRO graph to you.

See the command line help for more details:

.. code-block::

    mro-graph --help

As importable component
-----------------------

You can also do it this way:

.. code-block::

    from mro_graph import MROGraph

    MROGraph(dict)

This will generate and display the MRO graph of Python's builtin dictionary.
By using it this way, you can inspect live objects right inside your program.

License
=======

Copyright (C) 2003 Michele Simionato

Copyright (C) 2019-2020 Heiko 'riot' Weinen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

