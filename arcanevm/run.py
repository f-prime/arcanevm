from number import Number
from tape import Tape
from virtual_machine import VirtualMachine
import nufhe
import pprint


def run():
    ctx = nufhe.Context()
    secret_key, cloud_key = ctx.make_key_pair()
    vm = ctx.make_virtual_machine(cloud_key) 

    # Create tape
    # Create VM
    # Execute instruction
    # Get output tape encrypted
    # Decrypt tape to get execution results

    tape = Tape()
    
    # Create tape of size n
    
    n = 2

    indices = [] # Encrypt indices before feeding into VM
    for x in range(n):
        tape.add_cell(Number.from_plaintext(0, ctx, secret_key, vm))
        indices.append(Number.from_plaintext(x, ctx, secret_key, vm))

    flag = Number.from_plaintext(1, ctx, secret_key, vm, size=1) # Flag for conditions
    one = Number.from_plaintext(1, ctx, secret_key, vm, size=1) # A one
    zero = Number.from_plaintext(0, ctx, secret_key, vm, size=1) # A zero
    data_ptr = Number.from_plaintext(0, ctx, secret_key, vm)  # Cell to perform op on

    blind_machine = VirtualMachine(tape, data_ptr, flag, one, zero, indices)
    
    # Add 1 instruction

    inc_data_ptr = Number.from_plaintext(0, ctx, secret_key, vm)
    inc_data_cell = Number.from_plaintext(1, ctx, secret_key, vm)

    blind_machine.step(inc_data_ptr, inc_data_cell)

    pprint.pprint(tape.decrypt_tape(ctx, secret_key))

if __name__ == "__main__":
    run()
