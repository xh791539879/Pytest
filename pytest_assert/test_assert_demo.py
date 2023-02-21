import pytest

def test_demo1():
    a = 1
    assert a

def test_demo2():
    a = 0
    assert not a

def test_demo3():
    s = 'hello'
    assert 'h' in s

def test_demo4():
    a = 3
    assert a == 3

def test_demo5():
    a = 4
    assert a != 3

if __name__ == '__main__':
    pytest.main()