from nufhe import Context, lwe, api_low_level
from number import Number
from typing import List


class Tape(object):
    def __init__(
        self,
        context: Context,
        secret_key: api_low_level.NuFHESecretKey,
        length: int = 10,
    ):
        self.context: Context = context
        self.length: int = length
        self.secret_key: api_low_level.NuFHESecretKey = secret_key
        self.tape: List[Number] = self.generate_tape()

    def generate_tape(self) -> List[lwe.LweSampleArray]:
        tape: List[Number] = []

        for x in range(self.length):
            tape.append(Number(0, context=self.context, secret_key=self.secret_key))

        return tape

    def decrypt_tape(self) -> List[List[int]]:
        return [
            Number.decrypt(self.context, self.secret_key, cell.encrypted_binary)
            for cell in self.tape
        ]
