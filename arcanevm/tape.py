from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List


class Tape(object):
    def __init__(self, tape = []):
        self.tape = tape
   
    def add_cell(self, number):
        self.tape.append(number)

    def decrypt_tape(self, secret_key):
        return [
            cell.decrypt(secret_key)
            for cell in self.tape
        ]
