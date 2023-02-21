import pytest
@pytest.fixture()
def test_fixture():
    a="hello"
    print("这是conftest")
    yield a