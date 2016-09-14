# -*- coding: utf-8 -*-

import pytest
import wsinfo


def test_website():
    # Add URLs you want to test to this list
    for url in ["http://github.com"]:
        w = wsinfo.Info(url)

        if url == "http://github.com":
            # TODO keep this up to date with the generated Module contents list
            assert w.content != ""
            assert w.favicon_path == \
                "https://assets-cdn.github.com/favicon.ico"
            assert w.hierarchy == []
            assert w.http_header != ""  # TODO find a way to test this
            assert w.http_status_code == 200
            assert w.ip in ["192.30.253." + str(i) for i in [112, 113]]
            assert w.server == ["GitHub.com", None]
            assert w.server_os is None
            with pytest.raises(NotImplementedError):
                assert w.server_country
            with pytest.raises(ValueError):
                assert w.server_software
            assert w.title == "How people build software · GitHub"
            assert w.url == "https://github.com/"

        elif url == "http://localhost":
            assert w.content != ""
            assert w.favicon_path == "/dashboard/images/favicon.png"
            assert [x[0] for x in w.hierarchy] == ["h1", "h1", "h2",
                                                   "h3", "h3", "h3"]
            assert w.http_header != ""
            assert w.http_status_code == 200
            assert w.ip == "127.0.0.1"
            assert w.server[0] == "Apache"
            assert w.server_os == "Unix"
            with pytest.raises(NotImplementedError):
                assert w.server_country
            assert len(w.server_software) > 0
            assert w.title == "Welcome to XAMPP"
            assert w.url == "http://localhost/dashboard/"
