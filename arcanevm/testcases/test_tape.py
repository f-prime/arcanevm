import unittest
from tape import Tape
from number import Number
import nufhe

class TestTape(unittest.TestCase):
    def setUp(self):
        self.context = nufhe.Context()
        self.sk, self.ck = self.context.make_key_pair()

        self.one = Number.from_plaintext(1, self.context, self.sk)
        self.zero = Number.from_plaintext(0, self.context, self.sk)

    def test_create_tape(self):
        tape = Tape()

        self.assertEqual(tape.tape, [])

    def test_add_cell(self):
        tape = Tape()
        tape.add_cell(self.zero)
        tape.add_cell(self.one)

        self.assertEqual(tape.decrypt_tape(self.context, self.sk), [[[0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [1]]])
