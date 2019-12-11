from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List


class VirtualMachine(object):
    def __init__(self, tape, data_ptr, flag, one, zero, encrypted_indices):
        self.tape = tape
        self.data_ptr = data_ptr
        self.flag = flag
        self.one = one
        self.zero = zero
        self.encrypted_indices = encrypted_indices

    def step(self, inc_data_ptr, inc_data_cell):
        for i, encrypted_index in enumerate(self.encrypted_indices):
            flag = self.flag | self.one # Set flag to 1

            encrypted_binary = self.tape.tape[i]

            flag = flag & ~(encrypted_index ^ self.data_ptr) # Check if index equals pointer
            inc_data_cell_anded = inc_data_cell & flag
            self.tape.tape[i] = self.tape.tape[i] ^ inc_data_cell_anded

            print("Cell:", i, "processed") 
