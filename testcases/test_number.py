from arcanevm import number


def test_convert_binary():
    num1 = number.Number(128)
    num2 = number.Number(256)
    num3 = number.Number(512)
    num4 = number.Number(10)

    assert num1.binary == [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    assert num2.binary == [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert num3.binary == [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert num4.binary == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
