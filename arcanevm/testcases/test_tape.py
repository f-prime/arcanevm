import unittest
from tape import Tape
from number import Number
from contexts.FakeContext import FakeContext

class TestTape(unittest.TestCase):
    def setUp(self):
        self.context = FakeContext()
        self.sk = self.context.generate_keys()

        self.one = Number.from_plaintext(1, self.context, self.sk)
        self.zero = Number.from_plaintext(0, self.context, self.sk)

    def test_create_tape(self):
        tape = Tape()

        self.assertEqual(tape.tape, [])

    def test_add_cell(self):
        tape = Tape()
        tape.add_cell(self.zero)
        tape.add_cell(self.one)

        self.assertEqual(tape.decrypt_tape(self.sk), [0, 1])
