import unittest
from number import Number
from contexts.FakeContext import FakeContext
import utils

class TestNumber(unittest.TestCase):
    def setUp(self):
        self.context = FakeContext() 
        self.sk = self.context.generate_keys()

        self.one = Number.from_plaintext(1, self.context, self.sk)
        self.two = Number.from_plaintext(2, self.context, self.sk)
        self.three = Number.from_plaintext(3, self.context, self.sk)
        self.zero = Number.from_plaintext(0, self.context, self.sk)

        utils.zero = Number.from_plaintext(0, self.context, self.sk, size=1)
        utils.one = Number.from_plaintext(1, self.context, self.sk, size=1)


    def test_binary(self):
        one = Number.create_binary_array(1, 8)
        two = Number.create_binary_array(2, 8)
        three = Number.create_binary_array(3, 8)
        two56 = Number.create_binary_array(256, 8)

        flag = Number.create_binary_array(1, 1)

        self.assertEqual(two56, [[1],[0],[0],[0],[0],[0],[0],[0]])
        self.assertEqual(one, [[0],[0],[0],[0],[0],[0],[0],[1]])
        self.assertEqual(two, [[0],[0],[0],[0],[0],[0],[1],[0]])
        self.assertEqual(three, [[0],[0],[0],[0],[0],[0],[1],[1]])
        self.assertEqual(flag, [[1]])

    def test_and(self):
        one_and_two = self.one & self.two
        two_and_three = self.two & self.three
        one_and_three = self.one & self.three

        self.assertEqual(one_and_two.decrypt(self.sk, decimal=True), 0)
        self.assertEqual(two_and_three.decrypt(self.sk,decimal=True), 2)
        self.assertEqual(one_and_three.decrypt(self.sk, decimal=True), 1)

    def test_or(self):
        one_or_two = self.one | self.two
        two_or_three = self.two | self.three
        one_or_three = self.one | self.three

        self.assertEqual(one_or_two.decrypt(self.sk, decimal=True), 3)
        self.assertEqual(two_or_three.decrypt(self.sk, decimal=True), 3)
        self.assertEqual(one_or_three.decrypt(self.sk, decimal=True), 3)

    def test_xor(self):
        one_xor_two = self.one ^ self.two
        two_xor_three = self.two ^ self.three
        one_xor_three = self.one ^ self.three

        self.assertEqual(one_xor_two.decrypt(self.sk, decimal=True), 3)
        self.assertEqual(two_xor_three.decrypt(self.sk, decimal=True), 1)
        self.assertEqual(one_xor_three.decrypt(self.sk, decimal=True), 2)
   
    def test_not(self):
        not_zero = ~self.zero
        not_one = ~self.one

        self.assertEqual(not_zero.decrypt(self.sk, decimal=True), 255)
        self.assertEqual(not_one.decrypt(self.sk, decimal=True), 254)

    def test_add(self):
        one_plus_one = self.one + self.one
        three_plus_two = self.three + self.two
        three_plus_three = self.three + self.three
      
        self.assertEqual(one_plus_one.decrypt(self.sk, decimal=True), 2)
        self.assertEqual(three_plus_two.decrypt(self.sk, decimal=True), 5)
        self.assertEqual(three_plus_three.decrypt(self.sk, decimal=True), 6)

    def test_increment(self):
        zero_inc = self.zero.increment()
        one_inc = self.one.increment()
        two_inc = self.two.increment()
        three_inc = self.three.increment()

        self.assertEqual(zero_inc.decrypt(self.sk, decimal=True), 1)
        self.assertEqual(one_inc.decrypt(self.sk, decimal=True), 2)
        self.assertEqual(two_inc.decrypt(self.sk, decimal=True), 3)
        self.assertEqual(three_inc.decrypt(self.sk, decimal=True), 4)

    def test_decrement(self):
        one_dec = self.one.decrement()
        two_dec = self.two.decrement()
        three_dec = self.three.decrement()

        self.assertEqual(one_dec.decrypt(self.sk, decimal=True), 0)
        self.assertEqual(two_dec.decrypt(self.sk, decimal=True), 1)
        self.assertEqual(three_dec.decrypt(self.sk, decimal=True), 2)

    def test_from_plaintext(self):
        one28 = Number.from_plaintext(128, self.context, self.sk)
        too_big = Number.from_plaintext(512, self.context, self.sk, size=8)
       
        self.assertEqual(too_big.decrypt(self.sk, decimal=True), 128)
        self.assertEqual(one28.decrypt(self.sk, decimal=True), 128)

    def test_decrypt(self):
        self.assertEqual(self.one.decrypt(self.sk, decimal=True), 1)
        self.assertEqual(self.two.decrypt(self.sk, decimal=True), 2)
