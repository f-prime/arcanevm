
class Number(object):
    def __init__(self, logic, bit_array):
        self.bit_array = bit_array
        self.logic = logic

    @staticmethod
    def from_plaintext(number, context, secret, logic):
        array = Number.create_binary_array(number)
        for i, bit in enumerate(array):
            array[i] = context.encrypt(secret, bit)
        return Number(logic, array) 
    
    @staticmethod
    def create_binary_array(number):
        binary = []

        while number > 0:
            binary.insert(0, [number % 2])
            number //= 2

        while len(binary) < 8:
            binary.insert(0, [0])

        binary = binary[:8]  # All numbers are 8 bits

        return binary


    def decrypt(self, secret, context):
        output = []

        for bit in self.bit_array:
            output.append(list(map(int, context.decrypt(secret, bit))))

        return output

    def __do_operation(self, bit_array, op):
        output = []
        for i, bit in enumerate(bit_array):
            output.append(op(bit, self.bit_array[i]))
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


