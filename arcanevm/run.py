from number import Number
from tape import Tape
from virtual_machine import VirtualMachine
from contexts.NUFHEContext import NUFHEContext
from contexts.FakeContext import FakeContext
import pprint
import utils

def run():
    ctx = NUFHEContext()
    #ctx = FakeContext()
    
    secret_key = ctx.generate_keys()

    # Create tape with size of 2
    
    tape = Tape()
    tape_indices = tape.generate_tape(2, ctx, secret_key)

    utils.flag = Number.from_plaintext(1, ctx, secret_key, size=1)
    utils.one = Number.from_plaintext(1, ctx, secret_key, size=1)
    utils.zero = Number.from_plaintext(0, ctx, secret_key, size=1)

    # Initial state of machine

    data_ptr = Number.from_plaintext(0, ctx, secret_key)
    instruction_ptr = Number.from_plaintext(0, ctx, secret_key)

    # Defines instructions
    
    inc_data_ptr = Number.from_plaintext(1, ctx, secret_key)
    inc_data_cell = Number.from_plaintext(2, ctx, secret_key)
    dec_data_ptr = Number.from_plaintext(3, ctx, secret_key)
    dec_data_cell = Number.from_plaintext(4, ctx, secret_key)
    mark_loop = Number.from_plaintext(5, ctx, secret_key)
    loop_back = Number.from_plaintext(6, ctx, secret_key)


    instruction_set = {
        "+":inc_data_cell,
        "-":dec_data_cell,
        ">":inc_data_ptr,
        "<":dec_data_ptr,
        "[":mark_loop,
        "]":loop_back
    }

    instructions, instruction_indices = VirtualMachine.compile("++[>+++<-]", instruction_set, ctx, secret_key)

    blind_machine = VirtualMachine(
            tape,
            tape_indices,
            instruction_indices,
            instruction_set,
            instructions,
            instruction_ptr,
            data_ptr
    )

    

    blind_machine.run()

    pprint.pprint(tape.decrypt_tape(secret_key))


if __name__ == "__main__":
    run()
