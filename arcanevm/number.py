from typing import List
from nufhe import Context, lwe, api_low_level


class Number(object):
    def __init__(
        self,
        number: int,
        context: Context = None,
        secret_key: api_low_level.NuFHESecretKey = None,
    ):
        self.number: int = number
        self.binary: List[int] = self.create_binary_array()
        self.context: Context = context
        self.secret_key: api_low_level.NuFHESecretKey = secret_key

    def create_binary_array(self) -> List[int]:
        binary: List[int] = []
        number: int = self.number

        while number > 0:
            binary.insert(0, number % 2)
            number //= 2

        while len(binary) < 16:
            binary.insert(0, 0)

        binary = binary[:16]  # All numbers are 16 bits

        return binary

    def encrypt(self) -> lwe.LweSampleArray:
        return self.context.encrypt(self.secret_key, self.binary)

    @staticmethod
    def decrypt(
        context: Context,
        secret_key: api_low_level.NuFHESecretKey,
        data: lwe.LweSampleArray,
    ) -> List[int]:
        return list(map(int, context.decrypt(secret_key, data)))