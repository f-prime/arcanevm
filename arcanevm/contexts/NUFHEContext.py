import nufhe
import context

class NUFHEContext(context.Context):
    def __init__(self, cloud_key=None, ctx=None):
        self.cloud_key = cloud_key
        self.ctx = ctx
        self.vm = None

        if cloud_key and ctx:
            self.vm = ctx.make_virtual_machine(cloud_key)

    def decrypt(self, secret_key, bit):
        return self.ctx.decrypt(secret_key, bit)

    def encrypt(self, secret_key, bit):
        return self.ctx.encrypt(secret_key, bit)
   
    def generate_context(self):
        return nufhe.Context()
    
    def generate_keys(self):
        ctx = self.generate_context()
        secret, cloud_key = ctx.make_key_pair()
        
        self.ctx = ctx
        self.cloud_key = cloud_key
        self.vm = ctx.make_virtual_machine(cloud_key)
        
        return secret
    
    def gate_nand(self, bit1, bit2):
        return self.vm.gate_nand(bit1, bit2)

    def gate_nor(self, bit1, bit2):
        return self.vm.gate_nor(bit1, bit2)

    def gate_mux(self, bit1, bit2, bit3):
        return self.vm.gate_mux(bit1, bit2, bit3)

    def gate_and(self, bit1, bit2):
        return self.vm.gate_and(bit1, bit2)

    def gate_or(self, bit1, bit2):
        return self.vm.gate_or(bit1, bit2)

    def gate_xor(self, bit1, bit2):
        return self.vm.gate_xor(bit1, bit2)

    def gate_not(self, bit):
        return self.vm.gate_not(bit)
