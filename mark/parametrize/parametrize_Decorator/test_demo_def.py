import pytest
#装饰函数
@pytest.mark.parametrize("username,password",[("admin1","123456"),("admin2","12345678")])
def test_demo(username,password):
    print("账号:{},密码:{}".format(username,password))

#装饰测试函数时比较灵活，如果函数不使用数据就可以不装饰
