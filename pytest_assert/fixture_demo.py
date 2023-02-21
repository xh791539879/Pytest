import pytest

#module 级别
@pytest.fixture(scope="module")
def test_fixture():
    a = "hellow"
    print("在当前文件下执行一次")
    yield a
def test_01(test_fixture):
    print("这是test01")
    assert "e" in test_fixture
@pytest.mark.usefixtures("test_fixture")
class TestDemo:
    def test_demo01(self,test_fixture):
        print("这是test_demo01")
        assert "h" in test_fixture
    def test_demo02(self,test_fixture):
        print("这是test_demo02")
        assert "o" in test_fixture

