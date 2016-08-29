The wsinfo library
==================

wsinfo (short for website information) is a Python package for getting some
useful information about some website, without the need to write some
complicated hackish Python code.

The package is compatible with both Python 2 and 3.

Usage
-----

The usage of the wsinfo library is as easy as::

    >>> import wsinfo
    >>> w = wsinfo.Info("https://github.com")
    >>> w.http_status_code
    200
    >>> w.title
    'How people build software · GitHub'
    >>> w.content
    '<!DOCTYPE html>\n<html>\n[...]\n</html>'
