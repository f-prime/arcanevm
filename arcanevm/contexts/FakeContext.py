import context

class FakeContext(context.Context):
    def __init__(self, cloud_key=None, ctx=None):
        pass

    def decrypt(self, secret_key, bit):
        if type(bit) == list:
            return bit
        return [bit]

    def encrypt(self, secret_key, bit):
        return bit

    def generate_context(self):
        return None    

    def generate_keys(self):
        return "FakeContext"
   
    def convert_to_int(self, bit):
        if type(bit) == int:
            return bit
        elif type(bit) == list:
            return self.convert_to_int(bit[0])
        return bit

    def gate_xnor(self, bit1, bit2):
        return int(not (self.convert_to_int(bit1) ^ self.convert_to_int(bit2)))

    def gate_nor(self, bit1, bit2):
        return int(not (self.convert_to_int(bit1) | self.convert_to_int(bit2)))

    def gate_nand(self, bit1, bit2):
        return int(not(self.convert_to_int(bit1) & self.convert_to_int(bit2)))

    def gate_mux(self, bit1, bit2, bit3):
        bit1 = self.convert_to_int(bit1)
        bit2 = self.convert_to_int(bit2)
        bit3 = self.convert_to_int(bit3)

        return (bit1 & bit2) | ((not bit1) & bit3)

    def gate_and(self, bit1, bit2):
        return self.convert_to_int(bit1) & self.convert_to_int(bit2)

    def gate_or(self, bit1, bit2):
        return self.convert_to_int(bit1) | self.convert_to_int(bit2)

    def gate_xor(self, bit1, bit2):
        return self.convert_to_int(bit1) ^ self.convert_to_int(bit2)

    def gate_not(self, bit):
        return int(not self.convert_to_int(bit))
