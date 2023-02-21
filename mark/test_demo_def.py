#只跳过其中一个方法

import  pytest
class Test_demo():
    def test_demo01(self):
        print("这是test_demo01")
    @pytest.mark.skip(reason="功能未实现，暂不执行了")
    def test_demo02(self):
        print("这是test_demo02")