from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List
import utils

class VirtualMachine(object):
    def __init__(self, tape, encrypted_indices):
        self.tape = tape
        self.encrypted_indices = encrypted_indices

    def step(self, inc_data_ptr, inc_data_cell):
        for i, encrypted_index in enumerate(self.encrypted_indices):
            flag = utils.flag | utils.one # Set flag to 1

            encrypted_binary = self.tape.tape[i]

            flag = flag & ~(encrypted_index ^ utils.data_ptr) # Check if index equals pointer
            inc_data_cell_anded = inc_data_cell & flag
            self.tape.tape[i] = self.tape.tape[i] + inc_data_cell_anded

            print("Cell:", i, "processed") 
