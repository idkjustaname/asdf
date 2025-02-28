import unittest

def multiply(a, b):
    return a * b

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
