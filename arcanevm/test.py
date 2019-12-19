from contexts.NUFHEContext import NUFHEContext
import nufhe

ctx = NUFHEContext()
secret = ctx.generate_keys()

print(ctx.encrypt(secret, 1))
