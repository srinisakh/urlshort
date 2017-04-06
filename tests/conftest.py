import pytest

from urlshort.urlshort import create_app
from urlshort.models import db


@pytest.fixture()
def testapp(request):
    app = create_app('../tests/test-urlshort.cfg')
    client = app.test_client()

    db.app = app
    db.create_all()

    def teardown():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(teardown)

    return client

