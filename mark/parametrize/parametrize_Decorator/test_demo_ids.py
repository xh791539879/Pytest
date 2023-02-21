import pytest
data_01 = [
    (1, 2, 3),
    (4, 5, 9)
]
ids = ["a:{} + b:{} =expext:{}".format(a, b, expect)for a, b, expect in data_01]
def add(a, b):
    return a+b
@pytest.mark.parametrize('a, b, expect',data_01, ids=ids)
def test_parametrize_1(a, b, expect):
    print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
    assert add(a, b) == expect