import pytest


def test_demo_msg():
    n = 1
    while True:
        print("当前的值为{}".format(n))
        n+=1
        if n==4:  #跳过的值
            pytest.skip("跳过的值为{}".format(n))