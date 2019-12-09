from arcanevm import number
from nufhe import Context

def test_convert_binary():
    num1 = number.Number(1)
    num2 = number.Number(2)
    num3 = number.Number(5)
    num4 = number.Number(7)
    num5 = number.Number(128)

    assert(num1.binary == [[0],[0],[0],[0],[0],[0],[0],[1]])
    assert(num2.binary == [[0],[0],[0],[0],[0],[0],[1],[0]])
    assert(num3.binary == [[0],[0],[0],[0],[0],[1],[0],[1]])
    assert(num4.binary == [[0],[0],[0],[0],[0],[1],[1],[1]])
    assert(num5.binary == [[1],[0],[0],[0],[0],[0],[0],[0]])

    print("Convert binary test passed.")

def test_encrypt():
    ctx = Context()
    secret_key, cloud_key = ctx.make_key_pair()

    num = number.Number(13, context=ctx, secret_key=secret_key)

    encrypted = num.encrypt()

    assert(number.Number.decrypt(ctx, secret_key, encrypted) == [[0], [0], [0], [0], [1], [1], [0], [1]])
    
    print("Test encrypt data passed.")
