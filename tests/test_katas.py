import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 3), 2 + 3)

    def test_multiply(self):
        self.assertEqual(katas.multiply(4, 6), 4 * 6)

    def test_power(self):
        self.assertEqual(katas.power(2, 6), 2 ** 6)

    def test_factorial(self):
        self.assertTrue(katas.factorial(10))

    def test_fibonacci(self):
        self.assertTrue(katas.fibonacci(10))


if __name__ == '__main__':
    unittest.main()
