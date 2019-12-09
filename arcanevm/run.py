from number import Number
import nufhe


def run() -> None:
    ctx: nufhe.Context = nufhe.Context()
    secret_key, cloud_key = ctx.make_key_pair()

    # Create tape
    # Create VM
    # Execute instruction
    # Get output tape encrypted
    # Decrypt tape to get execution results

    num: Number = Number(123, context=ctx, secret_key=secret_key)

    enc = num.encrypt()

    print(Number.decrypt(ctx, secret_key, enc))
    print(num.binary)


if __name__ == "__main__":
    run()
