import nufhe
import random

# Compares two binary numbers and sets the flag to 1 or 0 based on whether the two numbers are equal

ctx = nufhe.Context()
secret_key, cloud_key = ctx.make_key_pair()
vm = ctx.make_virtual_machine(cloud_key)

print(secret_key, cloud_key)

DATA_POINTER = [[1], [0], [0], [1]]
CURRENT_INDEX = [[1], [0], [0], [1]]
FLAG = [1]

# Encrypt individual bits

for i, bit in enumerate(DATA_POINTER):
    DATA_POINTER[i] = ctx.encrypt(secret_key, bit)

for i, bit in enumerate(CURRENT_INDEX):
    CURRENT_INDEX[i] = ctx.encrypt(secret_key, bit)

FLAG = ctx.encrypt(secret_key, FLAG)

# compare

for i, bit in enumerate(DATA_POINTER):
    FLAG = vm.gate_and(FLAG, vm.gate_xnor(CURRENT_INDEX[i], DATA_POINTER[i]))

print(ctx.decrypt(secret_key, FLAG))
