import pytest


@pytest.mark.usefixtures("testapp")
class TestURLs:
    def test_home(self, testapp):
        """ Tests if the home page loads """

        rv = testapp.get('/')
        assert rv.status_code == 200

    def test_shorten_invalid(self, testapp):

        rv = testapp.post("/shorten?long_url=123")
        assert rv.status_code == 400

    def test_shorten_valid(self, testapp):

        rv = testapp.post("/shorten?long_url=http://google.com")
        assert rv.status_code == 200
