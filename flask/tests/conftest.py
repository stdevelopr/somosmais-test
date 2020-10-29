import pytest
from app import create_app

@pytest.yield_fixture(scope='session')
def app():
    _app = create_app({
        'TESTING': True,
        'ENV': 'test',
        'DEBUG': True
    })

    return _app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()