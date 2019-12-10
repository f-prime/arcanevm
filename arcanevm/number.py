from typing import List
from nufhe import Context, lwe, api_low_level

class Number(object):
    def __init__(
        self,
        number: int,
        context: Context = None,
        secret_key: api_low_level.NuFHESecretKey = None,
    ):
    
        self.context: Context = context
        self.secret_key: api_low_level.NuFHESecretKey = secret_key
        self.number: int = number
        self.binary: List[List[int]] = self.create_binary_array()
        if secret_key:
            self.encrypted_binary: List[List[lwe.LweSampleArray]] = self.encrypt()

    def create_binary_array(self) -> List[int]:
        binary: List[int] = []
        number: int = self.number

        while number > 0:
            binary.insert(0, [number % 2])
            number //= 2

        while len(binary) < 8:
            binary.insert(0, [0])

        binary = binary[:8]  # All numbers are 8 bits

        return binary

    def encrypt(self) -> List[lwe.LweSampleArray]:
        self.encrypted_binary = [self.context.encrypt(self.secret_key, bit) for bit in self.binary]
        return self.encrypted_binary

    @staticmethod
    def decrypt(
        context: Context,
        secret_key: api_low_level.NuFHESecretKey,
        data: lwe.LweSampleArray,
    ) -> List[List[int]]:
        
        output = []

        for element in data:
            output.append(
                list(map(int, context.decrypt(secret_key, element)))
            )

        return output
