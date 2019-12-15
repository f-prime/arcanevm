import unittest
from testcases.test_number import TestNumber
from testcases.test_tape import TestTape
from testcases.test_vm import TestVirtualMachine

def test_suite():
    suite = unittest.TestSuite()
    
    suite.addTest(TestNumber("test_binary"))
    suite.addTest(TestNumber("test_and"))
    suite.addTest(TestNumber("test_or"))
    suite.addTest(TestNumber("test_xor"))
    suite.addTest(TestNumber("test_not"))
    suite.addTest(TestNumber("test_add"))
    suite.addTest(TestNumber("test_from_plaintext"))
    suite.addTest(TestNumber("test_decrypt"))
    
    suite.addTest(TestTape("test_create_tape"))
    suite.addTest(TestTape("test_add_cell"))

    suite.addTest(TestVirtualMachine("test_machine_step"))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
