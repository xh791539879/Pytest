import pytest
#列表嵌套字典
dict_01 =[
    {"username":"admin1","password":"12345"},
    {"username":"admin2","password":"1234567"},
]
@pytest.mark.parametrize("dict",dict_01)
def test_login(dict):
    print("账号:{},密码:{}".format(dict["username"],dict["password"]))