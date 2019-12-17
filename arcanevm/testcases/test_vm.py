import unittest
from number import Number
from tape import Tape
from virtual_machine import VirtualMachine
import nufhe
import utils

class TestVirtualMachine(unittest.TestCase):
    def setUp(self):
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

        self.blind_machine = VirtualMachine(tape, indices)
        self.context = ctx
        self.secret_key = secret_key
        self.tape = tape

    def test_machine_step(self):
        incr_data_ptr = Number.from_plaintext(0, self.context, self.secret_key)
        inc_data_cell = Number.from_plaintext(1, self.context, self.secret_key)

        self.blind_machine.step(incr_data_ptr, inc_data_cell)

        self.assertEqual(self.tape.decrypt_tape(self.context, self.secret_key), [[[0], [0], [0], [0], [0], [0], [0], [1]], [[0], [0], [0], [0], [0], [0], [0], [0]]])
