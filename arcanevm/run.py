from typing import List
from number import Number
from tape import Tape
from virtual_machine import VirtualMachine
import nufhe
import pprint


def run() -> None:
    ctx: nufhe.Context = nufhe.Context()
    secret_key, cloud_key = ctx.make_key_pair()

    # Create tape
    # Create VM
    # Execute instruction
    # Get output tape encrypted
    # Decrypt tape to get execution results

    vm = ctx.make_virtual_machine(cloud_key)

    tape: List[nufhe.lwe.LweSampleArray] = Tape(ctx, secret_key, length=3)

    vm: VirtualMachine = VirtualMachine(ctx, vm, secret_key, tape, data_ptr=1)

    inc_data_ptr: Number = Number(0, context=ctx, secret_key=secret_key)
    inc_data_cell: Number = Number(1, context=ctx, secret_key=secret_key)

    vm.step(inc_data_ptr, inc_data_cell)

    pprint.pprint(tape.decrypt_tape())


if __name__ == "__main__":
    run()
