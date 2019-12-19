from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List
import utils

class VirtualMachine(object):
    def __init__(self, tape, encrypted_indices, instruction_set):
        self.tape = tape
        self.instruction_set = instruction_set
        self.encrypted_indices = encrypted_indices

    def step(self, instruction_on):
        new_dp = utils.data_ptr
        new_ip = utils.instruction_ptr

        for i, encrypted_index in enumerate(self.encrypted_indices):
            flag = utils.flag | utils.one # Set flag to 1

            encrypted_binary = self.tape.tape[i]

            is_correct_index = flag & ~(encrypted_index ^ utils.data_ptr) # Check if index equals pointer

            for instruction in self.instruction_set:
                is_correct_instruction = flag & ~(self.instruction_set[instruction] ^ instruction_on)
                
                should_process = is_correct_instruction & is_correct_index


                if instruction == "+":
                    self.tape.tape[i] = self.tape.tape[i].increment(to_inc_flag=should_process)

                elif instruction == "-":
                    self.tape.tape[i] = self.tape.tape[i].decrement(to_dec_flag=should_process)
                
                elif instruction == ">":
                    new_dp = utils.data_ptr.increment(to_inc_flag=is_correct_instruction)
                
                elif instruction == "<":
                    unew_dp = utils.data_ptr.decrement(to_dec_flag=is_correct_instruction)

                #input()

            print("Cell:", i, "processed")

        utils.data_ptr = new_dp
        utils.instruction_ptr = new_ip
