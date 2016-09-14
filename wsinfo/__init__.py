"""
The wsinfo library bundles the power of the ``socket`` module, some
``urllib`` subpackages, XML parsing and regular expressions into one library
with the possibility to get a huge amount of information for a specific
website.
"""

__version__ = "1.2.0"
__author__ = "Linus Groh"
__license__ = "MIT license"

import sys
import re
import socket
from xml.etree import ElementTree

PY2 = sys.version_info[0] == 2

if PY2:
    from urlparse import urlparse
    from urllib2 import urlopen, URLError, HTTPError
else:
    from urllib.parse import urlparse
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError


def _validate_url(url):
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
        r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    match_result = pattern.match(url)

    if not match_result:
        return False
    return True


class Info:
    """Class collecting some information about the website located at the
    given URL.

    :param url: Valid URL to the website *(e.g.
                http://example.com/path/to/file.html)*.
    """
    def __init__(self, url):
        self._url = url

        # Make sure that the given URL is valid
        if not _validate_url(self._url):
            raise ValueError("'{}' is not a valid URL".format(self._url))

        # Open URL and catch exceptions
        try:
            self._site = urlopen(self._url)
        except HTTPError as e:
            self._site = e
        except URLError as e:
            raise URLError(e.reason)

        # Process the file-like object we got
        if PY2:
            self._content = self._site.read()
        else:
            # Try multiple encodings
            for codec in ["utf-8", "utf-16", "utf-32",
                          "latin-1", "cp1251", "ascii"]:
                try:
                    self._content = self._site.read().decode(codec)
                    # Decoding successful, break look
                    break
                except UnicodeDecodeError:
                    # Decoding failed, try another one
                    continue

    @property
    def url(self):
        """Get the website's URL.

        .. note::
           **This will not always return the URL you've passed to the**
           ``Info`` **constructor.** For example, the server may redirect
           to another page, and this function will return the URL of the
           website you was redirected to. If the website implements a client
           side redirect, you will not be redirected but get the URL you've
           passed before.

           **Example for clarification:**

           Using a fresh install of a recent *XAMPP*, ``http://localhost``
           will redirect to ``http://localhost/dashboard/``::

               >>> import wsinfo
               >>> w = wsinfo.Info("http://localhost")
               >>> w.url
               'http://localhost/dashboard/'

           The original URL you've passed to the ``Info`` constructor is
           stored in the class attribute ``_url``::

               >>> w._url
               'http://localhost'

        :return: URL of the website.
        :rtype: str
        """
        return self._site.geturl()

    @property
    def ip(self):
        """Get the IP address of the website's domain.

        .. note::
           **This will not always return the IP address of the URL you've
           passed to the** ``Info`` **constructor.** For example, the
           server may redirect to another page, and this function will
           return the IP address of the redirected URL. If the website
           implements a client side redirect, you will not be redirected
           but get the IP address of the URL you've passed before.

        :return: IP address of the website's domain.
        :rtype: str
        """
        return socket.gethostbyname(urlparse(self.url).netloc)

    @property
    def http_status_code(self):
        """Get the website's HTTP status code.

        - **1xx:** Information
        - **2xx:** Success
        - **3xx:** Redirection
        - **4xx:** Client error
        - **5xx:** Server error

        See `this Wikipedia article <https://en.wikipedia.org/wiki/
        List_of_HTTP_status_codes>`_ for reference.

        :return: HTTP status code of the website.
        :rtype: int
        """
        return self._site.getcode()

    @property
    def http_header(self):
        """Get the website's HTTP header.

        :return: HTTP header of the website.
        :rtype: str
        """
        return str(self._site.headers)

    @property
    def title(self):
        """Get the website's title.

        The content of the first ``<title>`` tag in the HTML code is used.

        :return: The title of the website.
        :rtype: str
        """
        # Search for title tag
        pattern = re.compile(r"<title.*?>(.*?)</title>",
                             re.IGNORECASE | re.DOTALL)
        match = re.search(pattern, self._content)
        if match is not None:
            return match.group(1)
        return ""

    @property
    def content(self):
        """Get the website's content.

        :return: Content of the website *(e.g. HTML code)*.
        :rtype: str
        """
        return self._content

    @property
    def content_type(self):
        """Get the website's content type.

        :return: Content-type of the website's code *(e.g. text/html)*.
        :rtype: str or NoneType
        """
        return self._site.info()["Content-Type"]

    @property
    def favicon_path(self):
        """Get the path to the website's icon.

        The ``href`` attribute of the first ``<link>`` tag containing
        ``rel="icon"`` or ``rel="shortcut icon"`` is used.

        :return: The path to the icon of the website *(known as favicon*).
        :rtype: str or NoneType
        """
        # Iterate over all found <link> tags
        pattern = re.compile(r"<link.*?>", re.IGNORECASE | re.DOTALL)
        for tag in pattern.findall(self._content):
            # Form HTML to valid XML
            if not tag.endswith("<link/>"):
                tag = tag.replace("/>", ">")
                tag += "</link>"

            # Return href attribute if rel is one of 'icon', 'shortcut icon'
            root = ElementTree.fromstring(tag)
            if root.get("rel") in ["icon", "shortcut icon"]:
                return root.get("href")
        return None

    @property
    def hierarchy(self):
        """Get a list representing the heading hierarchy.

        :return: List of tuples containing the heading type *(h1, h2, ...)*
                 and the headings text.
        :rtype: list
        """
        # Iterate over all found <h1> - <h6> tags
        pattern = re.compile(r"<h(?P<n>[1-6])>(.*?)</h(?P=n)>",
                             re.IGNORECASE | re.DOTALL)
        return [("h{}".format(nr), text) for nr, text in
                pattern.findall(self._content)]

    @property
    def server(self):
        """Get the server's name/type and version.

        Most common are *Apache*, *nginx*, *Microsoft IIS* and *gws* on Google
        servers.

        :return: A list containing the name or type of the server software and
                 (if available) the version number.
        :rtype: list or NoneType
        """
        info = self._site.info()["Server"]
        if info:
            info = info.split("/", 1)
            if len(info) < 2:
                info.append(None)
            if type(info[1]) == str:
                pattern = re.compile(r"\((.*?)\)")
                info[1] = pattern.sub("", info[1]).split("  ")[0].strip()
            return info
        else:
            return None

    @property
    def server_software(self):
        """Get a list of the server's software stack.

        .. note:: This does only work for localhosts, because most public
           servers don't list any software configuration in the HTTP response
           header.

        :return: List of tuples containing both name and version for each
                 software listed in the http header.
        :rtype: list
        """
        pattern = re.compile(r".*?\.?localhost:?.*?",
                             re.IGNORECASE | re.DOTALL)
        if not pattern.match(urlparse(self.url).netloc.lower()):
            raise ValueError("this works only for localhosts, got '{}'"
                             .format(urlparse(self.url).netloc))
        software = []
        pattern = re.compile(r"(\S*)/(\S*)")
        for line in self.http_header.splitlines():
            if line.startswith("Server:"):
                line = line[7:].strip()
                for pair in pattern.findall(line):
                    software.append(pair)
        return software

    @property
    def server_os(self):
        """Get the operating system the server is running on.

        :return: The name of the servers OS.
        :rtype: str or NoneType
        """
        server = self._site.info()["Server"]
        pattern = re.compile(r".*?\((.*?)\)")
        if not pattern.match(server):
            return None
        else:
            return pattern.match(server).group(1)

    @property
    def server_country(self):
        """Get the country the where the server is located.

        .. warning::
           This is currently not implemented, I need to do some more research
           how to do this. I think *whois* is a buzzword...

        :return: The country where the server hardware is located.
        :rtype: str
        """
        raise NotImplementedError
