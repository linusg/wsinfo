The wsinfo library
==================

.. image:: https://api.travis-ci.org/linusg/wsinfo.svg?branch=master
   :target: https://travis-ci.org/linusg/wsinfo/
   :alt: Travis CI test status

.. image:: https://landscape.io/github/linusg/wsinfo/master/landscape.svg?style=flat
   :target: https://landscape.io/github/linusg/wsinfo/master
   :alt: Code health

.. image:: https://img.shields.io/pypi/v/wsinfo.svg
   :target: https://pypi.python.org/pypi/wsinfo
   :alt: Version

.. image:: https://img.shields.io/pypi/dm/wsinfo.svg
   :target: https://pypi.python.org/pypi/wsinfo
   :alt: Monthly downloads

wsinfo (short for website information) is a Python package for getting some
useful information about some website, without the need to write some
complicated hackish Python code.

Requirements
------------

The package is compatible with both Python 2 and 3, so everything you need is
a recent Python installation.

Installation
------------

The wsinfo library is available on `PyPI <http://pypi.python.org/pypi/wsinfo>`_,
so you can install it using ``pip``::

    pip install wsinfo

Usage
-----

The usage of the wsinfo library is as easy as::

    >>> import wsinfo
    >>> w = wsinfo.Info("https://github.com")
    >>> w.ip
    '192.30.253.112'
    >>> w.http_status_code
    200
    >>> w.title
    'How people build software · GitHub'
    >>> w.content
    '<!DOCTYPE html>\n<html>\n[...]\n</html>'

Tested Platforms and Python Versions
------------------------------------

The code was tested with the following software configurations:

+------------------+---------------------------+--------------------+
| **Platform**     | **Python implementation** | **Python version** |
+------------------+---------------------------+--------------------+
+ Ubuntu 16.04 LTS | CPython                   | 2.7.12             |
+------------------+---------------------------+--------------------+
+ Ubuntu 16.04 LTS | CPython                   | 3.5.2              |
+------------------+---------------------------+--------------------+
+ Ubuntu 16.04 LTS | PyPy 5.1.2                | 2.7.10             |
+------------------+---------------------------+--------------------+
+ Windows 7        | CPython                   | 2.7.12             |
+------------------+---------------------------+--------------------+

...but should work across all common platforms on Python 2.7 and 3.x. Other
success reports are welcome.