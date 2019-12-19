from bit import Bit
import utils

class Number(object):
    def __init__(self, encrypted_bit_array):
        self.encrypted_bit_array = encrypted_bit_array

    @staticmethod
    def from_plaintext(number, ctx, secret, size=8):
        array = Number.create_binary_array(number, size)
        for i, bit in enumerate(array):
            array[i] = Bit.from_plaintext(bit, ctx, secret) 
        return Number(array) 
   
    @staticmethod
    def from_bit(bit):
        return Number([bit])

    @staticmethod
    def create_binary_array(number, size):
        binary = []

        while number > 0:
            binary.insert(0, [number % 2])
            number //= 2
        
        while len(binary) < size:
            binary.insert(0, [0])

        binary = binary[:size]

        return binary


    def decrypt(self, secret, decimal=False):
        output = []

        for bit in self.encrypted_bit_array:
            output.append(bit.decrypt(secret))

        if decimal:
            s = 0
            for i, num in enumerate(output[::-1]):
                if num:
                    s += 2 ** i
            return s
        return output

    def __do_operation(self, encrypted_bit_array, op):
        iterate = encrypted_bit_array
        other = self.encrypted_bit_array
        is_bit = None
    
        if len(self.encrypted_bit_array) == 1:
            is_bit = other[0]
        
        elif len(encrypted_bit_array) == 1:
            iterate = self.encrypted_bit_array
            other = encrypted_bit_array
            is_bit = other[0]

        elif len(encrypted_bit_array) != len(self.encrypted_bit_array):
            raise ValueError("Number objects must be the same size")
        
        output = []

        for i, bit1 in enumerate(iterate):
            bit2 = is_bit if is_bit else other[i]

            if op == '&':
                result = bit1 & bit2
            elif op == '|':
                result = bit1 | bit2
            elif op == '^':
                result = bit1 ^ bit2
            else:
                raise ValueError(f"Invalid operation {op}")
            
            if is_bit:
                is_bit = result
            else:
                output.append(result)
        
        if is_bit:
            return Number.from_bit(is_bit)
        return Number(output)

    def __str__(self):
        return f"Number(size={len(self.encrypted_bit_array)})"

    def __and__(self, num):
        return self.__do_operation(num.encrypted_bit_array, '&')

    def __or__(self, num):
        return self.__do_operation(num.encrypted_bit_array, '|')

    def __xor__(self, num):
        return self.__do_operation(num.encrypted_bit_array, '^')

    def __invert__(self):
        return Number([~bit for bit in self.encrypted_bit_array])

    def __add__(self, num):
        carry = Bit.from_number(utils.zero)
        
        output = []
        
        # Treverse in reverse
    
        for bit_i in range(len(self.encrypted_bit_array))[::-1]:
            bit_1 = self.encrypted_bit_array[bit_i]
            bit_2 = num.encrypted_bit_array[bit_i]
            
            output.append(bit_1 ^ bit_2 ^ carry)
            carry = (bit_1 & bit_2) | (carry & (bit_1 ^ bit_2))
        
        return Number(output[::-1])

    def __sub__(self, num):
        raise NotImplemented("Subtraction is not yet implemented.")
    
    def mux(self, num1, num2):
        len1 = len(self.encrypted_bit_array)
        len2 = len(num1.encrypted_bit_array)
        len3 = len(num2.encrypted_bit_array)
        is_bit = None

        if len2 != len3:
            raise ValueError("Num1 and Num2 need to be the same size")
        
        if len1 != 1 and (len1 != len2 or len1 != len3):
            raise ValueError("Number must be either the same size as other inputs or of size 1")

        elif len1 == 1:
            is_bit = self.encrypted_bit_array[0]

        output = []

        for i, bit in enumerate(num1.encrypted_bit_array):
            bit1 = is_bit if is_bit else self.encrypted_bit_array[i]
            bit2 = num2.encrypted_bit_array[i]

            output.append(bit1.mux(bit, bit2))
        
        return Number(output)

    def increment(self, to_inc_flag=None):
        carry = Bit.from_number(utils.one)
        if to_inc_flag:
            carry = Bit.from_number(to_inc_flag) & carry
        
        output = []

        for bit_i in range(len(self.encrypted_bit_array))[::-1]:
            bit_1 = self.encrypted_bit_array[bit_i]
            output.append((bit_1 ^ carry))
            carry = bit_1 & carry

        return Number(output[::-1])

    def decrement(self, to_dec_flag=None):
        borrow = Bit.from_number(utils.one)
        if to_dec_flag:
            borrow = Bit.from_number(to_dec_flag) & borrow

        output = []

        for bit_i in range(len(self.encrypted_bit_array))[::-1]:
            bit_1 = self.encrypted_bit_array[bit_i]
            output.append((bit_1 ^ borrow))
            borrow = ~bit_1 & borrow

        return Number(output[::-1])

    def __mul__(self, num):
        raise NotImplemented("Multiply not yet implemented")

    def __truediv__(self, num):
        raise NotImplemented("Divide not yet implemented")


