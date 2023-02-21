import pytest
#列表嵌套元组
tuple_01 =[
    ("admin1","123456"),
    ("admin2","12345678"),
]
@pytest.mark.parametrize("username,password",tuple_01)
def test_login(username,password):
    print("账号:{},密码:{}".format(username,password))