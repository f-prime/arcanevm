import utils

class Number(object):
    def __init__(self, bit_array):
        if type(bit_array) != list:
            bit_array = [bit_array]
        self.bit_array = bit_array

    @staticmethod
    def from_plaintext(number, context, secret, size=8):
        array = Number.create_binary_array(number, size)
        for i, bit in enumerate(array):
            array[i] = context.encrypt(secret, bit)
        return Number(array) 
    
    @staticmethod
    def create_binary_array(number, size):
        binary = []

        while number > 0:
            binary.insert(0, [number % 2])
            number //= 2
        
        while len(binary) < size:
            binary.insert(0, [0])

        binary = binary[:size]  # All numbers are 8 bits

        return binary


    def decrypt(self, context, secret, decimal=False):
        output = []

        for bit in self.bit_array:
            output.append(list(map(int, context.decrypt(secret, bit))))

        if decimal:
            s = 0
            for i, num in enumerate(output[::-1]):
                if num[0]:
                    s += 2 ** i
            return s
        return output

    def __do_operation(self, bit_array, op):
        if (len(bit_array) != 1 and len(self.bit_array) != 1) and len(bit_array) != len(self.bit_array):
            raise ValueError("Bit arrays different sizes.")
        
        iterate_over = bit_array
        if len(bit_array) == 1:
            iterate_over = self.bit_array
        else:
            bit_array = self.bit_array

        output = []
        for i, bit in enumerate(iterate_over):
            bit_on = bit_array[0] if len(bit_array) == 1 else bit_array[i]
            output.append(op(bit, bit_on))
        
        return Number(output)

    def __str__(self):
        return f"Number(size={len(self.bit_array)})"

    def __and__(self, num):
        return self.__do_operation(num.bit_array, utils.logic.gate_and)

    def __or__(self, num):
        return self.__do_operation(num.bit_array, utils.logic.gate_or)

    def __xor__(self, num):
        return self.__do_operation(num.bit_array, utils.logic.gate_xor)

    def __invert__(self):
        return Number([utils.logic.gate_not(bit) for bit in self.bit_array])

    def __add__(self, num):
        carry = Number(utils.zero.bit_array)
        
        output = []
        
        # Treverse in reverse
    
        for bit_i in range(len(self.bit_array))[::-1]:
            bit_1 = Number(self.bit_array[bit_i])
            bit_2 = Number(num.bit_array[bit_i])
           
            output.append((bit_1 ^ bit_2 ^ carry).bit_array[0])
            carry = (bit_1 & bit_2) | (carry & (bit_1 ^ bit_2))
        
        return Number(output[::-1])

    def __sub__(self, num):
        borrow = Number(utils.one.bit_array)

        output = []
        print("SUBTRACT")

        # Traverse in reverse

        for bit_i in range(len(self.bit_array))[::-1]:
            bit_1 = Number(self.bit_array[bit_i])
            bit_2 = Number(num.bit_array[bit_i])

            output.append(((bit_1 ^ bit_2) ^ borrow).bit_array[0])
            borrow = (~bit_1 & borrow) + (~bit_1 & bit_2) + (bit_2 & borrow) # Figure out this borrow 

        return Number(output)
    def __mul__(self, num):
        raise NotImplemented("Multiply not yet implemented")

    def __truediv__(self, num):
        raise NotImplemented("Divide not yet implemented")


