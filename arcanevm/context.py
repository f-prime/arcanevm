"""
Generic context class
"""

from abc import ABC, abstractmethod

class Context(ABC):
    
    @abstractmethod
    def decrypt(self, secret_key, number):
        pass

    @abstractmethod
    def encrypt(self, secret_key, number):
        pass

    @abstractmethod
    def generate_context():
        pass
   
    @abstractmethod
    def gate_mux(self, bit1, bit2, bit3):
        pass

    @abstractmethod
    def gate_nor(self, bit1, bit2):
        pass
    
    def gate_nand(self, bit1, bit2):
        pass

    @abstractmethod
    def generate_keys():
        pass

    @abstractmethod
    def gate_and(self, bit1, bit2):
        pass

    @abstractmethod
    def gate_or(self, bit1, bit2):
        pass

    @abstractmethod
    def gate_xor(self, bit1, bit2):
        pass

    @abstractmethod
    def gate_not(self, bit):
        pass
