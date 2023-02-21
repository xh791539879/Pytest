import pytest
@pytest.mark.flaky(reruns =2,reruns_delay = 3)  #重试次数2,重试等待时间3
def test_demo():
    assert 3 == 4