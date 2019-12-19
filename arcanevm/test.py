from contexts.NUFHEContext import NUFHEContext
from bit import Bit
from number import Number
import utils

ctx = NUFHEContext()
secret = ctx.generate_keys()

bit = Bit.from_plaintext(1, ctx, secret)
bit2 = Bit.from_plaintext(0, ctx, secret)
print(bit)

utils.zero = bit2
utils.one = bit

b2 = bit ^ bit

print(b2.decrypt(secret))

num = Number.from_plaintext(5, ctx, secret)
print(num)
print("SUM")
num = num + num
print("INC")
num = num.increment()
print("INC")
num = num.increment()
print("DEC")
num = num.decrement()
print(num.decrypt(secret, decimal=True))
