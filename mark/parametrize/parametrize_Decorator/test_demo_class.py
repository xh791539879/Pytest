import pytest
#装饰类
@pytest.mark.parametrize("username,password",[("admin01","123456"),("admin02","123456789")])
class TestDemo:
    def test_demo(self,username,password):
        print("账号:{},密码:{}".format(username,password))

#注意：装饰测试类时，类内所有的方法必须接收测试数据，否则会报错；。