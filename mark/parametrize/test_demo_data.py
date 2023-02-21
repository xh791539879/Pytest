#单个数据
import pytest
data = ["小红", "小明"]
@pytest.mark.parametrize("name",data)
def test_demo(name):
    print("测试数据为{}".format(name))