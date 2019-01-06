import pytest

from api.red_flags import app

@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client
