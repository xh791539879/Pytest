# !/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

import pytest

class TestRegist:


    def test_regist(self):
        sleep(3)
        print("测试注册")

if __name__ == '__main__':
        pytest.main(['-vs'])