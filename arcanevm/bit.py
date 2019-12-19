class Bit(object):
    def __init__(self, ctx, encrypted_bit):
        self.ctx = ctx 
        self.encrypted_bit = encrypted_bit

    @staticmethod
    def from_plaintext(self, bit, ctx, secret_key):
        return Bit(ctx, self.ctx.encrypt(secret_key, bit)

    def decrypt(self, secret_key):
        return self.ctx.decrypt(secret_key, self.encrypted_bit)

    def __str__(self):
        return "Bit({self.encrypted_bit})"

    def __and__(self, bit1, bit2):
        return self.ctx.gate_and(bit1, bit2)

    def __or__(self, bit1, bit2):
        return self.ctx.gate_or(bit1, bit2)

    def __xor__(self, bit1, bit2):
        return self.ctx.gate_xor(bit1, bit2)

    def __invert__(self, bit):
        return self.ctx.gate_not(bit)
