# !/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

import pytest


class TestLogin:

    def test_login(self):
        sleep(3)
        print("测试登录")

if __name__ == '__main__':
        pytest.main()