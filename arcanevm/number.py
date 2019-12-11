
class Number(object):
    def __init__(self, logic, bit_array):
        self.bit_array = bit_array
        self.logic = logic

    @staticmethod
    def from_plaintext(number, context, secret, logic, size=8):
        array = Number.create_binary_array(number, size)
        for i, bit in enumerate(array):
            array[i] = context.encrypt(secret, bit)
        return Number(logic, array) 
    
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


    def decrypt(self, context, secret):
        output = []

        for bit in self.bit_array:
            output.append(list(map(int, context.decrypt(secret, bit))))

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
        return Number(self.logic, output)

    def __str__(self):
        return str(self.bit_array)

    def __and__(self, num):
        return self.__do_operation(num.bit_array, self.logic.gate_and)

    def __or__(self, num):
        return self.__do_operation(num.bit_array, self.logic.gate_or)

    def __xor__(self, num):
        return self.__do_operation(num.bit_array, self.logic.gate_xor)

    def __invert__(self):
        return Number(self.logic, [self.logic.gate_not(bit) for bit in self.bit_array])

    def __add__(self, num):
        raise NotImplemented("Add not yet implemented")

    def __sub__(self, num):
        raise NotImplemented("Subtraction not yet implemented") 

    def __mul__(self, num):
        raise NotImplemented("Multiply not yet implemented")

    def __truediv__(self, num):
        raise NotImplemented("Divide not yet implemented")


