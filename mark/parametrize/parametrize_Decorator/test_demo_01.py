import pytest
username = ["admin1","admin2","admin3"]
password = ["123456","123456789","abc123456"]

#使用多个参数化装饰器，数据会进行交叉组合的方式传递给测试函数，进而生成n*n个测试用例(笛卡尔积)。
@pytest.mark.parametrize("uname",username)
@pytest.mark.parametrize("pwd",password)
def test_demo(uname,pwd):
    print("账号:{},密码:{}".format(uname,pwd))