Usage
=====

#. Make sure you've :ref:`installed <installation>` the |wsinfo|
   library correctly.
#. Run Python and import the library::

    >>> import wsinfo

#. Create an instance of the ``Info`` class. I'll use the *GitHub* start
   page in the following examples::

    >>> w = wsinfo.Info("https://github.com")

#. Now you can get all the information::

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

   Also see the :ref:`API overview <api>` for reference.

   .. note::
      All public methods of the ``Info`` class are using the ``@property``
      decorator, so you'll not have to make function calls. Instead, they're
      treated as class attributes.

#. Full code::

    import wsinfo

    w = wsinfo.Info("https://github.com")
    print(w.http_status_code)
    print(w.title)
    print(w.content)

.. include:: global.rst
