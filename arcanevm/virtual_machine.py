from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List

class VirtualMachine(object):
    def __init__(self, context: Context, vm, secret_key: api_low_level.NuFHESecretKey, tape: List[lwe.LweSampleArray], data_ptr: int = 0):
        self.vm = vm
        self.context: Context = context
        self.data_ptr: Number = Number(data_ptr, context=context, secret_key=secret_key)  
        self.secret_key: api_low_level.NuFHESecretKey = secret_key
        self.tape = tape
    
    def step(self, inc_data_ptr, inc_data_cell):
        for index in range(len(self.tape.tape)):
            flag = self.context.encrypt(self.secret_key, [1])
             
            encrypted_index: Number = Number(index, context=self.context, secret_key=self.secret_key)
            encrypted_binary: List[int] = self.tape.tape[index].encrypted_binary

            for i, bit in enumerate(self.data_ptr.encrypted_binary):
                flag = self.vm.gate_and(self.vm.gate_xnor(encrypted_index.encrypted_binary[i], bit), flag) 
           
            print("Current flag value:", self.context.decrypt(self.secret_key, flag))

            cells: List[int] = self.tape.tape[index] # Current cell number
           
            # AND instruction with flag. If flag is 0 then wrong cell else correct cell

            inc_data_cell_anded = []

            for i in range(len(inc_data_cell.encrypted_binary)):
                inc_data_cell_anded.append(self.vm.gate_and(flag, inc_data_cell.encrypted_binary[i]))

            print("Instruction AND:", Number.decrypt(self.context, self.secret_key, inc_data_cell_anded))

            print("Cells", cells)
            for i in range(len(inc_data_cell_anded)):
                cells.encrypted_binary[i] = self.vm.gate_xor(inc_data_cell_anded[i], cells.encrypted_binary[i])
