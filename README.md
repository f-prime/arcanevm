# ArcaneVM

ArcaneVM is a virtual machine that can execute instructions encrypted with [Fully Homomorphic Encryption](https://blog.cryptographyengineering.com/2012/01/02/very-casual-introduction-to-fully/). Basically, it's a Brainfuck interpreter that can execute encrypted brainfuck code.

ArcaneVM relies on the [nufhe](https://github.com/nucypher/nufhe) library for its FHE implementation.

Join the chat on Matrix [#arcanevm:matrix.org](https://riot.im/app/#/room/#arcanevm:matrix.org)

# About

Fully Homomorphic Encryption (FHE) is a relatively new encryption technology that allows for computations on encrypted data. This allows us not only to encrypt the inputs but also encrypt the computations themselves. The output is also encrypted and when decrypted gives the plaintext result of the computation.

This is extremely powerful for people who not only have sensitive data, but also have computations that are sensitive.

Since the program essentially has zero context on what it is computing, it has to run through every possible branch of the program. On top of this, the underlying encryption schemes that make FHE possible are very computationally expensive.

What this means in the context of ArcaneVM and Brainfuck is that the more instructions a program has, and the larger the tape that it is working with, the slower the program is going to become.
This is because at every cycle, the VM has to go through every possible instruction on every possible data cell.

As a result, ArcaneVM is very very _very_ slow.

All integers in ArcaneVM are 8 bits.

# Example

### Execute Brainfuck code

```
from arcanevm import run

run("++[>+++<-]>>", tape_size=5)
```

# Dependencies

- Python 3
- PyOpenCL
- nufhe

# Build

```bash
sudo apt install python3-pyopencl
pip3 install -r requirements.txt
```
