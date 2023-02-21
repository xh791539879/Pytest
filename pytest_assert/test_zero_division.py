import pytest

# def test_zero_division():
#     1 / 0
# if __name__ == '__main__':
#     pytest.main()

#在测试过程中，有时需要对特定异常进行断言，可以使用 pytest.raises 作为上下文管理器，当抛出异常时可以获取到对应的异常实例。


#所以我们需要捕获并断言异常。
#断言场景：断言抛出的异常是否符合预期。
#预期结果：ZeroDivisionError: division by zero，其中ZeroDivisionError为错误类型，division by zero为具体错误值。
#断言方式:  断言异常的type和value值。
def test_zero_division_long():
    with pytest.raises(ZeroDivisionError) as excinfo:  #pytest.raises 捕获异常，
        1 / 0
    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    assert "division by zero" in str(excinfo.value) #excinfo作为异常信息实例，拥有type 、value等属性,excinfo.value的值是元组，所以要转成字符串。
if __name__ == '__main__':
    pytest.main()