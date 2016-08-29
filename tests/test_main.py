import pytest
import wsinfo


def test_website():
    url = "https://github.com"
    w = wsinfo.Info(url)

    # TODO keep this up to date with the generated Module contents list
    assert w.content != ""
    assert w.favicon_path == "https://assets-cdn.github.com/favicon.ico"
    assert w.http_header != ""  # TODO find a way to test this, e.g. regex
    assert w.http_status_code == 200
    assert w.ip in ["192.30.253." + str(i) for i in [112, 113]]
    with pytest.raises(NotImplementedError):
        assert w.server_country
    assert w.server == ""
    assert w.title == "How people build software · GitHub"
    assert w.url == url
