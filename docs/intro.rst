Introduction
============

In short...
-----------

The |wsinfo| library bundles the power of the ``socket`` module, some
``urllib`` subpackages, XML parsing and regular expressions into one library
with the possibility to get a huge amount of information for a specific
website.

Why should I use it?
--------------------

Did you ever had to retrieve information about some website? Maybe.

But then you know what a pain it is, if you want to do more than getting the
HTML code of a website. You will have to use a lot of different standard and
not standard library modules:

+--------------------+-----------------------------------------+
| **Python version** |  **Libraries**                          |
+--------------------+-----------------------------------------+
+      Python 2      | ``urlparse``, ``urllib``, ``urllib2``   |
+                    | and ``httplib``                         |
+--------------------+-----------------------------------------+
+      Python 3      | ``urllib3``, some subpackages of        |
+                    | ``urllib`` and ``http``                 |
+--------------------+-----------------------------------------+
+        Both        | ``socket``, ``requests`` and            |
+                    | ``beautifulsoup``                       |
+--------------------+-----------------------------------------+

Confused?

While some of the standard library modules were moved or replaced in Python 3
(see above), you will probably have to adapt your code to work under both
Python 2 and Python 3.

I don't want to talk about connection issues and the ton of HTTP error codes
you'll need to handle one day.

The next step then is parsing the HTML using an HTML or XML parser library,
or some difficult regular expressions. Not funny, because some web developers
don't care about HTML standards even today.

And that's why you can use the |wsinfo| library for getting website
information on the fly. It really makes your life easier, and your code
shorter.

How can I use it?
-----------------

The library works for both online and localhost websites, it's usage is as
easy as::

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

Pretty nice, huh?

.. include:: global.rst
