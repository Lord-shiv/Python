import unittest

from prime import is_prime


class Tests(unittest.TestCase):  # test class
    def test_1(self):
        ''' checks that no is prime or not'''
        self.assertFalse(is_prime(6))

    def test_2(self):
        ''' checks that no is prime or not'''
        self.assertTrue(is_prime(17))

    def test_3(self):
        ''' checks that no is prime or not'''
        self.assertFalse(is_prime(10))

    def test_4(self):
        ''' checks that no is prime or not'''
        self.assertTrue(is_prime(17))

    def test_5(self):
        ''' checks that no is prime or not'''
        self.assertFalse(is_prime(22))


if __name__ == "__main__":
    unittest.main()
