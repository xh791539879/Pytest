#整个类都跳过

import  pytest
@pytest.mark.skip(reason="功能暂时未实现，先不运行")
class Test_demo():
    def test_demo01(self):
        print("这是test_demo01")
    def test_demo02(self):
        print("这是test_demo02")