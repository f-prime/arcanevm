from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List


class Tape(object):
    def __init__(self, tape = None):
        if tape:
            self.tape = tape
        else:
            self.tape = []

    def add_cell(self, number):
        self.tape.append(number)

    def decrypt_tape(self, secret_key):
        return [
            cell.decrypt(secret_key, decimal=True)
            for cell in self.tape
        ]

    def generate_tape(self, size, ctx, secret_key):
        indices = [] # Encrypt indices before feeding into VM
        for x in range(size):
            self.add_cell(Number.from_plaintext(0, ctx, secret_key))
            indices.append(Number.from_plaintext(x, ctx, secret_key))

        return indices
