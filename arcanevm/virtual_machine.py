from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List
import utils

class VirtualMachine(object):
    def __init__(self, tape, encrypted_tape_indices, encrypted_instruction_indices, instruction_set, instructions, instruction_ptr, data_ptr):
        self.tape = tape
        self.instruction_set = instruction_set
        self.instructions = instructions
        self.instruction_ptr = instruction_ptr
        self.encrypted_tape_indices = encrypted_tape_indices
        self.encrypted_instruction_indices = encrypted_instruction_indices 
        
        self.instruction_ptr = instruction_ptr
        self.data_ptr = data_ptr
        
        self.loop_start = instruction_ptr

    def step(self, instruction_on, is_correct_instruction_ptr):
        new_dp = self.data_ptr

        for i, encrypted_index in enumerate(self.encrypted_tape_indices):
            flag = utils.one # Set flag to 1

            encrypted_binary = self.tape.tape[i]

            is_correct_index = flag & encrypted_index.xnor(self.data_ptr) # Check if index equals pointer
        
            for instruction in self.instruction_set:
                is_correct_instruction = flag & self.instruction_set[instruction].xnor(instruction_on)
                
                should_process = is_correct_instruction & is_correct_index & is_correct_instruction_ptr
                
                if instruction == "+":
                    self.tape.tape[i] = self.tape.tape[i].increment(to_inc_flag=should_process)

                elif instruction == "-":
                    self.tape.tape[i] = self.tape.tape[i].decrement(to_dec_flag=should_process)
                
                elif instruction == ">":
                    new_dp = new_dp.increment(to_inc_flag=should_process)
                
                elif instruction == "<":
                    new_dp = new_dp.decrement(to_dec_flag=should_process)

                elif instruction == "[":
                    self.loop_start = should_process.mux(self.instruction_ptr, self.loop_start) 

                elif instruction == "]":
                    should_process = should_process & (utils.zero | self.tape.tape[i])
                    self.instruction_ptr = should_process.mux(self.loop_start, self.instruction_ptr)
            

        self.data_ptr = new_dp

    def run(self):
        for step_num in range(50):
            print("Step Num", step_num)
            
            for i, instruction_i in enumerate(self.encrypted_instruction_indices):
                instruction = self.instructions[i]
                is_correct_instruction_ptr = utils.one & instruction_i.xnor(self.instruction_ptr)
                self.step(instruction, is_correct_instruction_ptr)
            
            self.instruction_ptr = self.instruction_ptr.increment()
    
    @staticmethod
    def compile(code, instruction_set, ctx, secret_key):
        instructions = []
        for char in code:
            if char in instruction_set:
                instructions.append(instruction_set[char])

        instruction_indices = []
        
        for i, _ in enumerate(instructions):
            instruction_indices.append(Number.from_plaintext(i, ctx, secret_key))

        return instructions, instruction_indices
