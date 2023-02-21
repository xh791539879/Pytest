
# -*- coding: UTF-8 -*-
import pytest

@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_demo():
    assert 3 == 4