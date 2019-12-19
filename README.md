# ArcaneVM

ArcaneVM is a virtual machine that can execute code encrypted with [Fully Homomorphic Encryption](https://blog.cryptographyengineering.com/2012/01/02/very-casual-introduction-to-fully/). Basically, it's a Brainfuck interpreter that can execute encrypted brainfuck code. 

ArcaneVM relies on the [nufhe](https://github.com/nucypher/nufhe) library for its FHE implementation.

# About

Fully Homomorphic Encryption (FHE) is a reletively new encryption technology that allows for computations on encrypted data. This allows us not only to encrypt the inputs but also encrypt the computation itself. The result is also encrypted and when decrypted gives the results of the computation. 
This is extremely powerful for people who not only have sensitve data, but also have computations that are sensative. 

The problem is that it is currently very very slow for a couple of reasons. Since the program essentially has zero context on what it is computing, it has to run through every possible branch of the program. Every possible way that the program can be run it has to run and this becomes slow very quickly. 
On top of this, the underlying encryption schemes that make FHE possible rely on systems that make the computations very expensive.

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

`sudo apt install python3-pyopencl`

`pip3 install -r requirements.txt`
