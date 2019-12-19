class Bit(object):
    def __init__(self, ctx, encrypted_bit):
        self.ctx = ctx 
        self.encrypted_bit = encrypted_bit

    @staticmethod
    def from_plaintext(bit, ctx, secret_key):
        return Bit(ctx, ctx.encrypt(secret_key, [bit]))
    
    @staticmethod
    def from_number(number):
        return number.encrypted_bit_array[-1]

    def decrypt(self, secret_key):
        return int(self.ctx.decrypt(secret_key, self.encrypted_bit)[0])

    def __str__(self):
        return f"Bit({self.encrypted_bit})"

    def __and__(self, bit2):
        return Bit(self.ctx, self.ctx.gate_and(self.encrypted_bit, bit2.encrypted_bit))

    def __or__(self, bit2):
        return Bit(self.ctx, self.ctx.gate_or(self.encrypted_bit, bit2.encrypted_bit))

    def __xor__(self, bit2):
        return Bit(self.ctx, self.ctx.gate_xor(self.encrypted_bit, bit2.encrypted_bit))

    def __invert__(self):
        return Bit(self.ctx, self.ctx.gate_not(self.encrypted_bit))

    def nand(self, bit2):
        return Bit(self.ctx, self.ctx.gate_nand(self.encrypted_bit, bit2.encrypted_bit))

    def nor(self, bit2):
        return Bit(self.ctx, self.ctx.gate_nor(self.encrypted_bit, bit2.encrypted_bit))

    def mux(self, bit2, bit3):
        return Bit(self.ctx, self.ctx.gate_mux(self.encrypted_bit, bit2.encrypted_bit, bit3.encrypted_bit))
