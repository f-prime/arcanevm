from number import Number
from tape import Tape
from virtual_machine import VirtualMachine
import nufhe
import pprint
import utils

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
        tape.add_cell(Number.from_plaintext(0, ctx, secret_key))
        indices.append(Number.from_plaintext(x, ctx, secret_key))

    utils.logic = vm
    utils.flag = Number.from_plaintext(1, ctx, secret_key, size=1) # Flag for conditions
    utils.one = Number.from_plaintext(1, ctx, secret_key, size=1) # A one
    utils.zero = Number.from_plaintext(0, ctx, secret_key, size=1) # A zero
    utils.data_ptr = Number.from_plaintext(0, ctx, secret_key)  # Cell to perform op on

    blind_machine = VirtualMachine(tape, indices)
    
    # Add 1 instruction
    
    
    """
    for x in range(3):
        inc_data_ptr = Number.from_plaintext(0, ctx, secret_key)
        inc_data_cell = Number.from_plaintext(1, ctx, secret_key)

        blind_machine.step(inc_data_ptr, inc_data_cell)
    

    """

    #print(utils.one + utils.one)
    
    A = 127
    B = 1

    sum = Number.from_plaintext(A, ctx, secret_key) + Number.from_plaintext(B, ctx, secret_key)
    diff = Number.from_plaintext(A, ctx, secret_key) - Number.from_plaintext(B, ctx, secret_key)

    print(sum.decrypt(ctx, secret_key))
    print(A, "+", B, "=", sum.decrypt(ctx, secret_key, decimal=True))
    print(diff.decrypt(ctx, secret_key))
    print(A, '-', B, "=", diff.decrypt(ctx, secret_key, decimal=True)) 


    #pprint.pprint(tape.decrypt_tape(ctx, secret_key))



if __name__ == "__main__":
    run()
